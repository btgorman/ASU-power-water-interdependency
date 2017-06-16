# AUTHOR: BRANDON T GORMAN
# DATE: MAY 18, 2017
# BUILT USING PYTHON 3.6.0
# STATUS: WORK IN PROGRESS

import numpy as np
import pandas as pd

class PumpLoad:
	CLID = 9000
	
	ID = 0
	TYPE = 1
	LOAD_ID = 2
	PUMP_ID = 3
	CHECK_LOAD_DEMAND = 4
	CHECK_PUMP_STATUS = 5

	def __init__(self, dframe):
		self.cols = list(dframe.columns)
		self.matrix = dframe.values
		self.num_components = len(dframe.index)
		self.num_switches = self.num_components * 0
		self.num_stochastic = self.num_components * 0
		self.switch_chance = (0.0, 0.0)
		self.stochastic_chance = (0.0, 0.0)

	def classValue(cls, str):
		try:
			return getattr(cls, str)
		except:
			print('INTERCONN ERROR in PumpLoad0')

	def PumpRow(self, ID):
		for row in self.matrix:
			if row[PumpLoad.PUMP_ID] == ID:
				return row
		return 0

	def LoadRow(self, ID):
		for row in self.matrix:
			if row[PumpLoad.LOAD_ID] == ID:
				return row
		return 0

class TankGenerator:
	CLID = 9001
	
	ID = 0
	TYPE = 1
	GENERATOR_ID = 2
	JUNCTION_ID = 3
	TANK_ID = 4
	CHECK_GENERATOR_PRODUCTION = 5
	CHECK_TANK_LEVEL = 6

	def __init__(self, dframe):
		self.cols = list(dframe.columns)
		self.matrix = dframe.values
		self.num_components = len(dframe.index)
		self.num_switches = self.num_components * 0
		self.num_stochastic = self.num_components * 0
		self.switch_chance = (0.0, 0.0)
		self.stochastic_chance = (0.0, 0.0)

	def classValue(cls, str):
		try:
			return getattr(cls, str)
		except:
			print('INTERCONN ERROR in TankGenerator0')

	def GeneratorRow(self, ID):
		for row in self.matrix:
			if row[TankGenerator.GENERATOR_ID] == ID:
				return row
		return 0

	def JunctionRow(self, ID):
		for row in self.matrix:
			if row[TankGenerator.JUNCTION_ID] == ID:
				return row
		return 0

	def TankRow(self, ID):
		for row in self.matrix:
			if row[TankGenerator.TANK_ID] == ID:
				return row
		return 0
