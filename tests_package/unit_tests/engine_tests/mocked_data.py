""" Module containing utils for test_engine.py """
# coding=utf-8
from argparse import Namespace
from os.path import dirname, join


class MockedData(object):

    @staticmethod
    def get_mocked_arg_parser():
        mocked_arg_parser = Namespace(
            description=None,
            filter=None,
            genre=None,
            gui='run',
            json=None,
            number=0,
            sort=None,
            title='a light in the attic')
        return mocked_arg_parser

    @staticmethod
    def get_expected_description():
        expected_description = """It's hard to imagine a world without A Light in the Attic. This now-classic collection of poetry and drawings from Shel Silverstein celebrates its 20th anniversary with this special edition. Silverstein's humorous and creative verse can amuse the dowdiest of readers. Lemon-faced adults and fidgety kids sit still and read these rhythmic words and laugh and smile and love th It's hard to imagine a world without A Light in the Attic. This now-classic collection of poetry and drawings from Shel Silverstein celebrates its 20th anniversary with this special edition. Silverstein's humorous and creative verse can amuse the dowdiest of readers. Lemon-faced adults and fidgety kids sit still and read these rhythmic words and laugh and smile and love that Silverstein. Need proof of his genius? RockabyeRockabye baby, in the treetopDon't you know a treetopIs no safe place to rock?And who put you up there,And your cradle, too?Baby, I think someone down here'sGot it in for you. Shel, you never sounded so good. ...more"""
        return expected_description

    @staticmethod
    def mocked_html_path_builder():
        project_root = dirname(dirname(__file__))
        output_path = join(project_root, 'engine_tests//mocked_html.html')
        with open(output_path, 'r') as html_file:
            test_html = html_file.read()
            return test_html

