from text_to_mp3_conversion.convert import _chunk_text


def test_empty_string():
    assert _chunk_text("") == []


def test_short_text_single_chunk():
    text = "Hello world"
    result = _chunk_text(text)
    assert result == ["Hello world"]


def test_text_split_into_multiple_chunks():
    word = "a" * 100
    # Build text that spans multiple 200-char chunks
    text = " ".join([word] * 10)  # 1009 chars
    result = _chunk_text(text, max_chars=200)
    assert len(result) > 1
    for chunk in result:
        assert len(chunk) <= 200


def test_no_word_is_broken():
    words = ["hello", "world", "foo", "bar", "baz"]
    text = " ".join(words * 100)
    result = _chunk_text(text, max_chars=20)
    all_words_in_result = " ".join(result).split(" ")
    for word in all_words_in_result:
        assert word in words


def test_all_words_preserved():
    text = "one two three four five six seven eight nine ten"
    result = _chunk_text(text, max_chars=15)
    assert " ".join(result) == text


def test_custom_max_chars():
    text = "ab cd ef gh ij"
    result = _chunk_text(text, max_chars=5)
    for chunk in result:
        assert len(chunk) <= 5


def test_single_word_exceeding_limit():
    long_word = "x" * 5000
    result = _chunk_text(long_word, max_chars=3000)
    assert result == [long_word]
