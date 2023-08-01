#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Hurricane - система поиска данных, OSINT разведки, криптографии и нетворкинга
Copyright (C) 2023  Okulus Dev
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""
import sys
from datetime import datetime

import libhurricane.security.fakeua as fakeua
import libhurricane.scanners.sqlinjection as sqlinj
import libhurricane.scanners.cve as cve
import libhurricane.scanners.xss as xss


class Hurricane:
	"""Класс системы поиска данных Hurricane"""
	def __init__(self):
		"""Инициализация класса"""

	def cve_search(self, request: str):
		"""Парсер CVE"""
		data = cve.search_cve(request)

		date = str(datetime.now()).split('.')[0].replace(' ', '_')
		print(f'Отчет записан в results/{date}_cve_{request}.txt')

		with open(f'{date}_cve_{request}.txt', 'w') as file:
			file.write(data)

		return data


def main():
	"""Главная функция"""

	if len(sys.argv) > 1:
		hurricane = Hurricane()


if __name__ == '__main__':
	main()
