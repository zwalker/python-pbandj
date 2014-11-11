#!python
# Copyright (c) 2009 Las Cumbres Observatory.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from setuptools import setup, find_packages

if __name__ == '__main__':

    setup(
        name = "pbandj",
        version = "2.0.3",
        packages=find_packages('.', exclude=['dummy']),
#        package_dir={'pbandj': 'pbandj'},
        install_requires = ['Django>=1.0.2-final','protobuf>=2.4.1',],#'protobuf.socketrpc>=1.3.2'],
        author = "Zachary Walker",
        author_email = "zwalker@lcogt.net",
        description = "Utility for creating Protocol Buffer Messages and RPC services from a Django model",)
