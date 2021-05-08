#-*- coding: utf-8 -*-

"""Python から Xpdf tools の pdftotext.exe を呼び出して抽出します。"""
 
import argparse
from pathlib import Path
from subprocess import run, PIPE
import csv
def pdf_reader(pdf_file,
               exe_file='C:\Program Files (x86)\tools\xpdf-tools-win-4.03\bin64\pdftotext.exe',
               xpdfrc_file = 'C:\Program Files (x86)\tools\xpdf-tools-win-4.03\xpdfrc'):
    """
    Arguments:
        filename: 入力のpdfファイル (str)
    Returns:
        company_name: 支払先
        payment_amount: 支払額
    """
    pdf_file = Path(pdf_file)
    exe_file = Path(exe_file)
    xpdfrc_file = Path(xpdfrc_file)
    cmd = (
        exe_file,
        '-cfg', xpdfrc_file,
        '-enc', 'UTF-8', # テキストを出力する時のエンコーディング
        # '-q', # メッセージやエラーを表示しない
        '-nopgbrk', # '-nopgbrk': テキストに改ページを表す文字列を付けない
        pdf_file,
        '-', # テキストを標準出力(stdout)に出す
    )
    cp = run(
        cmd,
        stdout=PIPE, # 標準出力からテキスト受け取るために PIPE を指定
    )
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
    initial_name = pdf_file[:2]
    if initial_name == 'HK1':
        company_name = text_list[7]
        payment_amount = (text_list[-1]).split()[-2:]
    elif initial_name == 'MY1':
        pass
    elif initial_name == 'MY2':
        pass
    elif initial_name == 'SG1':
        pass
    elif initial_name == 'SG2':
        pass
    elif initial_name == 'SG3':
        pass
    elif initial_name == 'SG4':
        pass
    elif initial_name == 'SG5':
        pass
    elif initial_name == 'TH1':
        pass
    elif initial_name == 'TW1':
        pass
    elif initial_name == 'TW2':
        pass
    elif initial_name == 'TW3':
        pass
    else:
        raise Exception('Unnexpected Error')
    print(company_name)
    print(payment_amount)
    return  company_name, payment_amount
def csv_reader(csv_file):
    print(csv_file)
    """
    Arguments:
        csv: 入力のCSVファイル (str)
    Returns:
        1列目の列名以外 (list)
    """
    with open(csv_file, 'r') as rf:
        csv_list = rf.read().split()[1:]
    return csv_list
def argparser():
    parser = argparse.ArgumentParser(description='PDFファイルを読み取って支払先と支払額を返すスクリプト')
    parser.add_argument('config_file', help='抽出対象のPDFリスト')
    parser.add_argument('output_csv', help='出力CSV名')
    return parser
def main(pdf_files, output_csv='Aggregate.csv'):
    """メイン関数"""
    for pdf_file in pdf_files:
        company_name, payment_amount = pdf_reader(pdf_file)
        with open(output_csv, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([company_name,payment_amount])
    # (終了)
    print(pdf_files)
    print('end')
if __name__ == "__main__":
    parser = argparser()
    args = parse.parse_args()
    # 引数のパース
    config_file = args.config_file
    output_csv = args.output_csv
    # configファイルの読み込み
    pdf_list = csv_reader(config_file)
    # main関数の実行
    main(pdf_list, output_csv)