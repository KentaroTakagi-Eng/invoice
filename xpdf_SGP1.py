"""Python から Xpdf tools の pdftotext.exe を呼び出して抽出します。"""

from pathlib import Path
from subprocess import run, PIPE

def main():
    """メイン関数"""

    # (1/7) PDF ファイルを決める
    pdf_file = Path(r'C:\Users\kntrt\OneDrive\ドキュメント\Python Scripts\invoice\SGP1B.pdf')
    ##pdf_file = Path(r'C:\Users\kntrt\OneDrive\デスクトップ\Sample Invoice\TWN2.pdf')
    # (2/7) 実行ファイル pdftotext.exe のファイルパスを決める
    exe_file = Path(r'C:\Program Files (x86)\tools\xpdf-tools-win-4.03\bin64\pdftotext.exe')

    # (3/7) 日本語サポートパッケージの xpdfrc のファイルパスを決める
    xpdfrc_file = Path(r'C:\Program Files (x86)\tools\xpdf-tools-win-4.03\xpdfrc')

    # (4/7) コマンドラインの引数リストを作る(タプルでもOK)
    # 構文: pdftotext [options] [PDF-file [text-file]]
    # テキストを標準出力(stdout)に出すときは、
    # [text-file] にハイフン '-' を指定するとのこと。
    cmd = (
        exe_file,
        '-cfg', xpdfrc_file,
        '-enc', 'UTF-8', # テキストを出力する時のエンコーディング
        # '-q', # メッセージやエラーを表示しない
        '-nopgbrk', # '-nopgbrk': テキストに改ページを表す文字列を付けない
        pdf_file,
        '-', # テキストを標準出力(stdout)に出す
        )

    # (5/7) PDF からテキストを抽出する
    # cp は CompletedProcess の略です。
    cp = run(
        cmd,
        stdout=PIPE, # 標準出力からテキスト受け取るために PIPE を指定
        )

    # (6/7) もし pdftotext.exe がエラーを返したときは知らせる
    if cp.returncode == 0:
        # 正常に終了した。
        # ただし、壊れたPDFでも 0 が返る。その代わり、処理中に
        # Syntax Error (50): Illegal character <2f> in hex string
        # などのエラーメッセージが表示された。
        # エラーメッセージは '-q' のオプションで非表示にできた。
        print(f'ok - {cp.returncode} - {pdf_file.name}')
    else:
        # なんらかのエラー error を検出した。
        # (例) PDFが開けなかった、テキストの出力ファイルが開けなかった、
        # PDFのパーミッションに関するエラーでPDFが開けなかった、など。
        print(f'error - {cp.returncode} - {pdf_file.name}')

    # (7/7) 抽出したテキストデータを受け取る & デコードする
    text = cp.stdout.decode('utf-8')
    text = text.strip() # 先頭と末尾の空白や改行を除去する
    text_list = text.split("\r\n")

    # (デバッグ情報)
    print(f'(デバッグ) exe_file: {exe_file}')
    print(f'(デバッグ) xpdfrc_file: {xpdfrc_file}')
    print(f'(デバッグ) pdf_file: {pdf_file}')
    print(f'(デバッグ) cp.returncode: {cp.returncode}')
    #print(f"(デバッグ) cp.stdout.decode('utf-8'):『\n{text_list}』")
    print((text_list[0]).split()[:2])
    print(text_list[-1])

    # (終了)
    print('end')
    return

if __name__ == "__main__":
    main()