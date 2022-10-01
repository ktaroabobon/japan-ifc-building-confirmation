import lzma
import base64


def zip_str(text: str, encoding: str = 'utf-8') -> str:
    """文字列を圧縮する関数

    Args:
        text (str): 対象文字列
        encoding (str): フォーマット形式

    Returns:
        str: 圧縮後の文字列
    """
    binary_data = text.encode(encoding=encoding)
    return base64.b85encode(lzma.compress(binary_data)).decode(encoding=encoding)


def unzip_str(text: str, encoding: str = 'utf-8') -> str:
    """圧縮された文字列を展開する関数

    Args:
        text (str): 圧縮された文字列
        encoding (bytes): フォーマット形式

    Returns:
        str: 展開後の文字列
    """
    binary_data = lzma.decompress(base64.b85decode(text))
    return binary_data.decode(encoding=encoding)
