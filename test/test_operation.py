# -*- coding: utf-8 -*-
# @Time    : 2021/3/18 10:14 下午
# @Author  : JiangYanQun
# @File    : test_operation.py
from ssh_operation import SshOperation


def test():
    host = '192.168.1.31'
    port = 22
    username = 'ps'
    pwd = '123456'
    ssh_op = SshOperation(host, port)
    ssh_op.ssh_connect_pwd(username, pwd)
    download_files = {'81220': '/data/netfs/baowu_test_data/81220_ff460cbe-e7e7-4933-a62b-6787f4136656'}
    for k, v in download_files.items():
        local_path = '/Users/yan/PycharmProjects/baowu_contract_extract/test_file/' + k + '.csv'
        remove_path = v + '/ocr/sentence_classification/all_contents.csv'
        try:
            ssh_op.download_file(remove_path, local_path)
            print(remove_path, '下载成功！')
        except Exception as e:
            print(e)
            print(remove_path, '文件不存在')
            remove_path = v + '/edit_pdf/sentence_classification/source_file_content.csv'

            try:
                ssh_op.download_file(remove_path, local_path)
                print(remove_path, '下载成功！')
            except Exception as e:
                print(e)
                print(remove_path, '文件不存在')

    ssh_op.close()


if __name__ == '__main__':
    test()