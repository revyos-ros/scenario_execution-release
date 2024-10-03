# Copyright (C) 2024 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions
# and limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

from setuptools import find_namespace_packages, setup

PACKAGE_NAME = 'scenario_execution_x11'

setup(
    name=PACKAGE_NAME,
    version='1.2.0',
    packages=find_namespace_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + PACKAGE_NAME]),
        ('share/' + PACKAGE_NAME, ['package.xml'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Intel Labs',
    maintainer_email='scenario-execution@intel.com',
    description='Scenario Execution library for X11',
    license='Apache License 2.0',
    tests_require=['pytest'],
    include_package_data=True,
    entry_points={
        'scenario_execution.actions': [
            'capture_screen = scenario_execution_x11.actions.capture_screen:CaptureScreen',
        ],
        'scenario_execution.osc_libraries': [
            'x11 = '
            'scenario_execution_x11.get_osc_library:get_osc_library',
        ]
    },
)
