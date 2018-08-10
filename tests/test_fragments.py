"""Test cases for the fragments module"""

import pytest

from gator import fragments


@pytest.mark.parametrize(
    "writing_string,expected_count",
    [
        ("hello world", 1),
        ("hello world!!%^()", 1),
        ("hello world!!%^(@after)", 1),
        ("hello world!!%^(@after)writing a lot", 1),
        ("hello world!!%^(@after)writing a lot\n", 1),
        ("hello world!!%^(@after)writing a lot\n\n", 1),
        ("", 0),
        ("", 0),
        (" ", 0),
        (" ", 0),
        ("     ", 0),
        ("     ", 0),
        ("a     ", 1),
        ("a     ", 1),
        ("a\n     ", 1),
        ("# Section Header", 0),
        ("# Section Header\n\nNot Section Header", 1),
        ("Paragraph\n\n\n# Section Header", 1),
        ("Paragraph\n\n```\nShould not be a paragraph\n```", 1),
        ("```\nShould not be\na paragraph\n```", 0),
        (
            "Beginning of paragraph ``` Still in fences but now \
    also in paragraph ``` and end",
            1,
        ),
    ],
)
def test_paragraphs_zero_or_one(writing_string, expected_count):
    """Check that it can detect zero or one paragraphs"""
    assert fragments.count_paragraphs(writing_string) == expected_count


@pytest.mark.parametrize(
    "writing_string,expected_count",
    [
        ("hello world!!%^(@after)writing a lot\n\nnew one", 2),
        ("hello world\n\nhi", 2),
        ("hello world\n\nhi\n\nff!$@name", 3),
        ("hello world\n\nhi\n\nff!$@name\n\n^^44", 4),
        ("hello world 44\n\nhi\n\nff!$@name\n\n^^44", 4),
        ("# Section Header\n\nhello world 44\n\nhi\n\nff!$@name\n\n^^44", 4),
    ],
)
def test_paragraphs_many(writing_string, expected_count):
    """Check that it can detect two or more paragraphs"""
    assert fragments.count_paragraphs(writing_string) == expected_count


@pytest.mark.parametrize(
    "writing_string,expected_count",
    [
        ("hello world! Writing a lot.\n\nsingle.", 1),
        ("hello world! Writing a lot.\n\nnew one.", 2),
        ("hello world! Writing a lot.\n\nNew one. Question?", 3),
        (
            "The method test.main was called. Hello world! Writing a lot.\n\n"
            "New one. Question? Fun!",
            4,
        ),
        (
            "New one. Question? Fun! Nice!\n\n"
            "The method test.main was called. Hello world! Writing a lot.",
            5,
        ),
        (
            "The method `test.main` was called. Hello world! Example? Writing.\n\n"
            "New one. Question? Fun! Nice!",
            5,
        ),
        (
            "The method test.main was called.\nHello world! Example? Writing.\n\n"
            "New one. Question? Fun! Nice!",
            5,
        ),
        (
            "Here is some code in a code block.\n\n```\ndef test_function():\n    "
            "function_call()\n```\n\nHello world! Example? Writing.\n\n"
            "New one. Question? Fun! Nice!",
            4,
        ),
        ("", 0),
    ],
)
def test_words_different_counts(writing_string, expected_count):
    """Check that it can detect different counts of words"""
    assert fragments.count_words(writing_string) == expected_count


@pytest.mark.parametrize(
    "writing_string,chosen_fragment,expected_count",
    [
        ("hello world!!%^(@after)writing a lot\n\nnew one", "writing", 1),
        ("hello @world!!%^(@after)writing a lot\n\nnew one", "@world", 1),
        ("hello world!!%^(@after)writing a lot\n\nnew one", "@world", 0),
        ("System.out.println(new Date())", "new Date()", 1),
        ("System.out.println(new Date())", "new Date", 1),
    ],
)
def test_chosen_fragment_zero_or_one(writing_string, chosen_fragment, expected_count):
    """Check that it can detect one or more of a fragment"""
    assert (
        fragments.count_specified_fragment(writing_string, chosen_fragment)
        == expected_count
    )


@pytest.mark.parametrize(
    "writing_string,chosen_fragment,expected_count",
    [
        ("hello world!!%^(@after)writing a lot\n\nnew one writing", "writing", 2),
        ("hello @world!!%^(@after)writing a lot\n\nnew new new one", "new", 3),
        ("hello @world!!%^(@after)writing a @world lot\n\nnew one", "@world", 2),
        ("System.out.println(new Date()) \n new Date()", "new Date()", 2),
        ("System.out.println(new Date() new Date() new Date())", "new Date", 3),
    ],
)
def test_chosen_fragment_many(writing_string, chosen_fragment, expected_count):
    """Check that it can detect many of a fragment"""
    assert (
        fragments.count_specified_fragment(writing_string, chosen_fragment)
        == expected_count
    )