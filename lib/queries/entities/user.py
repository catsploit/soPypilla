#!/usr/bin/python3
#-*- coding:utf-8 -*-

from dataclasses import dataclass


@dataclass
class UserInfo:
	direction: str
	city: str
	name: str
	rut: str
	sex: str


@dataclass
class VehicleInfo:
	patent: str
	typeof: str
	nmotor: int
	brand: str
	model: str
	owner: str
	year: int