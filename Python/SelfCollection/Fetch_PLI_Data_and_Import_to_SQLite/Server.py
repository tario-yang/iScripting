# coding: utf-8

'''
Connect PLI Server, then fetch data and import it to SQL Lite database.
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from win32com.client import Dispatch as CreateObject
import sqlite3


'''
WholeFields = {
	'Activity Inserted' : 'csh_pli_activity_inserted',
	'Additional Info' : 'csh_pli_additional_info',
	'Assembly or Device Serial No' : 'csh_pli_ass_or_device_serial_no',
	'Assigned Engineer' : 'csh_pli_assigned_to',
	'Assigned Owner' : 'owned_by_id',
	'Assigned To Verify' : 'csh_pli_assigned_to_verify',
	'Build Fixed' : 'csh_pli_build_fixed',
	'Build Found' : 'csh_pli_product_build_found',
	'Build Verified' : 'csh_pli_build_verified',
	'Built By' : 'csh_pli_built_by',
	'Classification' : 'classification',
	'Close/Postpone/Reject Reason' : 'csh_pli_postpone_or_close_reason',
	'Colsed Date' : 'csh_pli_closed_date',
	'csh_pli_hav_veri_procreslts_cq' : 'csh_pli_hav_veri_procreslts_cq',
	'Customer Complaint Number' : 'csh_pli_customer_complaint',
	'Customer Info' : 'csh_pli_customer_info',
	'Date Verified' : 'csh_pli_date_verified',
	'Description' : 'csh_pli_description',
	'Design Impact' : 'csh_pli_design_impact',
	'Detection Activity' : 'csh_pli_detection_activity',
	'Duplicate Of' : 'csh_pli_duplicate_of',
	'Effectiveness Check Plan' : 'csh_pli_effectiveness_check_plan',
	'Effectiveness Check Results' : 'csh_pli_effectiv_check_results',
	'Effectiveness Owner' : 'csh_pli_effectiveness_owner',
	'Evaluation' : 'csh_pli_evaluation',
	'Event Number' : 'csh_pli_event_number',
	'Expected Close Date' : 'csh_pli_expected_close_date',
	'Expected Resolve Date' : 'csh_pli_expected_resolve_date',
	'Field Modification' : 'csh_pli_field_modification',
	'Impact' : 'csh_pli_impact',
	'Implementation Priority' : 'csh_pli_implementation_priority',
	'Initial Reported Date' : 'csh_pli_initial_reported_date',
	'Is an Effectiveness Check Required' : 'csh_pli_effectiv_check_required',
	'Is ECR Required' : 'csh_pli_is_ecr_required',
	'Is there a Performance risk' : 'csh_pli_is_there_a_perf_risk',
	'Is there a Safety risk' : 'csh_pli_is_there_a_safety_risk',
	'Is This A Customer Complaint' : 'csh_pli_is_this_a_cust_complaint',
	'Issue Type' : 'csh_pli_issue_type',
	'Market Risk Assessment' : 'csh_pli_market_risk_assessment',
	'Method' : 'csh_pli_method',
	'OS Platform' : 'csh_pli_os_platform',
	'Part' : 'csh_pli_part',
	'Part Revision' : 'csh_pli_part_revision',
	'Parts On Hand' : 'csh_pli_parts_on_hand',
	'PC Models' : 'csh_pli_pc_models',
	'PCP Phase Detected' : 'csh_pli_pcp_phase_detected',
	'PCP Phase Inserted' : 'csh_pli_pcp_phase_inserted',
	'Performance Frequency' : 'csh_pli_performance_frequency',
	'Performance Risk' : 'csh_pli_performance_risk',
	'Performance Severity' : 'csh_pli_performance_severity',
	'Potential Reportable Event' : 'csh_pli_potent_reportable_event',
	'Preventative Action' : 'csh_pli_preventative_action',
	'Product' : 'csh_pli_product',
	'Product Module' : 'csh_pli_module',
	'Rationale' : 'csh_pli_rationale',
	'Rationale1' : 'csh_pli_rationale1',
	'Reason for No ECR Required' : 'csh_pli_preidentified_reasons',
	'Reason for No Effectiveness Check Required' : 'csh_pli_reason_no_effectiv_check',
	'Release To production' : 'csh_pli_release_to_production',
	'Reproducible' : 'csh_pli_reproducible',
	'Resolution Info' : 'csh_pli_resolution_info',
	'Responsibility' : 'csh_pli_responsibility',
	'Root Build' : 'csh_pli_root_build',
	'Root Cause Classification' : 'csh_pli_root_cause_classi',
	'Root Cause Description' : 'csh_pli_root_cause_description',
	'Root Version' : 'csh_pli_root_version',
	'Safety Frequency' : 'csh_pli_safety_frequency',
	'Safety Risk' : 'csh_pli_safety_risk',
	'Safety Severity' : 'csh_pli_safety_severity',
	'State' : 'state',
	'Submitted By' : 'created_by_id',
	'Submitted On' : 'created_on',
	'Subsystem/Subsystem Version' : 'csh_pli_subsystem_version',
	'System ID K# or S/N' : 'csh_pli_systemid_no_sn',
	'Title' : 'csh_pli_title',
	'Top Number' : 'csh_pli_top_number',
	'Verified By' : 'csh_pli_verified_by',
	'Verify Results' : 'csh_pli_verify_results',
	'Version Fixed' : 'csh_pli_version_fixed',
	'Version Found' : 'csh_pli_product_version_found',
	'Version To Be Fixed' : 'csh_pli_version_to_be_fixed',
	'Version Verified' : 'csh_pli_version_verified',
	'Was Resolution Effective' : 'csh_pli_was_resolution_effective',
	'Workaround' : 'csh_pli_workaround'}
'''
WholeFields = {
	'Event Number':						['text primary key', 'csh_pli_event_number'],
	'Title':							['text', 'csh_pli_title'],
	'State':							['text', 'state'],
	'Assigned Engineer':				['text', 'csh_pli_assigned_to'],
	'Assigned Owner':					['text', 'owned_by_id'],
	'Assigned To Verify':				['text', 'csh_pli_assigned_to_verify'],
	'Build Fixed':						['text', 'csh_pli_build_fixed'],
	'Build Found':						['text', 'csh_pli_product_build_found'],
	'Build Verified':					['text', 'csh_pli_build_verified'],
	'Built By':							['text', 'csh_pli_built_by'],
	'Classification':					['text', 'classification'],
	'Close/Postpone/Reject Reason':		['text', 'csh_pli_postpone_or_close_reason'],
	'Colsed Date':						['text', 'csh_pli_closed_date'],
	'Date Verified':					['text', 'csh_pli_date_verified'],
	'Description':						['text', 'csh_pli_description'],
	'Duplicate Of':						['text', 'csh_pli_duplicate_of'],
	'Impact':							['text', 'csh_pli_impact'],
	'OS Platform':						['text', 'csh_pli_os_platform'],
	'PC Models':						['text', 'csh_pli_pc_models'],
	'PCP Phase Detected':				['text', 'csh_pli_pcp_phase_detected'],
	'PCP Phase Inserted':				['text', 'csh_pli_pcp_phase_inserted'],
	'Performance Frequency':			['text', 'csh_pli_performance_frequency'],
	'Performance Risk':					['text', 'csh_pli_performance_risk'],
	'Performance Severity':				['text', 'csh_pli_performance_severity'],
	'Product':							['text', 'csh_pli_product'],
	'Product Module':					['text', 'csh_pli_module'],
	'Reproducible':						['text', 'csh_pli_reproducible'],
	'Responsibility':					['text', 'csh_pli_responsibility'],
	'Root Build':						['text', 'csh_pli_root_build'],
	'Root Cause Classification':		['text', 'csh_pli_root_cause_classi'],
	'Root Cause Description':			['text', 'csh_pli_root_cause_description'],
	'Root Version':						['text', 'csh_pli_root_version'],
	'Submitted By':						['text', 'created_by_id'],
	'Submitted On':						['text', 'created_on'],
	'Subsystem/Subsystem Version':		['text', 'csh_pli_subsystem_version'],
	'Verified By':						['text', 'csh_pli_verified_by'],
	'Verify Results':					['text', 'csh_pli_verify_results'],
	'Version Fixed':					['text', 'csh_pli_version_fixed'],
	'Version Found':					['text', 'csh_pli_product_version_found'],
	'Version To Be Fixed':				['text', 'csh_pli_version_to_be_fixed'],
	'Version Verified':					['text', 'csh_pli_version_verified'],
	'Workaround':						['text', 'csh_pli_workaround'],
}

class PLIServer:

	def __init__(self, product, operation_method='CSH_PLI_QueryDefect'):
		'''
		Value of product and operation_method shall be the one set in PLI
		'''
		self.IOMFactoryProgID = 'Aras.IOM.IomFactory.9.3'
		self.ServerAddress    = 'http://cs-pli.carestreamhealth.com/InnovatorServer'
		self.ServerDatabase   = 'PLIPROD'
		self.OperationMethod  = operation_method # for defect by default
		self.Product          = product
		self.WholeFieldString = ','.join([i for i in WholeFields.keys()])
		self.PLIServer        = CreateObject(self.IOMFactoryProgID)
		self.Connection       = self.PLIServer.CreateWinAuthHttpServerConnection(self.ServerAddress, self.ServerDatabase)

		if self.Connection.Login().IsError:
			return None
		else:
			self.innovator = self.PLIServer.CreateInnovator(self.Connection)

		self.Result = self.QueryResult()

	def QueryResult(self):
		print '[{}] Start to query data ...'.format(self.Product)
		datasource = self.QueryData(self.WholeQueryBody())
		retData    = []
		for i in xrange(datasource.getItemCount()):
			subRet = datasource.getItemByIndex(i)
			tmp = {}
			for key, value in WholeFields.items():
				tmp[key] = subRet.getProperty(value[1], '')
			retData.append(tmp)
		print '[{}] Queried!'.format(self.Product)
		return retData

	def QueryData(self,querybody):
		return self.innovator.applyMethod(self.OperationMethod, querybody)

	def WholeQueryBody(self):
		'''
		this function will generate a XML to query whole fields
		'''
		return '''<display>{0}</display>
		<sortfield>Event Number</sortfield>
		<sorttype>A</sorttype>
		<filter>AND</filter>
		<conditionCount>1</conditionCount>
		<condition0>Product,=,{1}</condition0>'''.format(self.WholeFieldString, self.Product)

	def ExportToCSV(self):
		pass

class SQLLiteServer:

	def __init__(self, database, table):
		self.Database   = database
		self.Table      = table
		self.PrimaryKey = 'Event Number'
		self.Connection = sqlite3.connect(self.Database)
		self.Fields     = self.DbBaseElement()
		self.KeyFields  = self.Fields.keys()

		if self.IsTableExisted() is True:
			print 'Table({}) has existed.'.format(self.Table)
		else:
			print 'Table({}) does not exist.'.format(self.Table)
			if self.DbCreateTable() is True:
				print 'Table({}) has created.'.format(self.Table)
			else:
				print 'Table({}) failed to be created.'.format(self.Table)
				return None

	def DbBaseElement(self):
		ret = WholeFields.copy()
		for key,value in ret.items():
			ret[key].append(key.replace(' ', '_').replace('/', '_'))
		return ret

	def IsTableExisted(self):
		try:
			cursor = self.Connection.cursor()
			cursor.execute('select count(*) from {};'.format(self.Table))
		except:
			return False
		else:
			return True

	def DbCreateTable(self):
		try:
			cursor = self.Connection.cursor()
			cursor.execute('create table {0}({1});'.format(self.Table,
				','.join(['{0} {1}'.format(i[1][-1], i[1][0]) for i in self.Fields.items()])))
		except:
			return False
		else:
			return True

	def DbUpdate(self, input_dict):
		'''
		input_dict shall be a dict
		'''
		key_fields = []
		for i in self.KeyFields:
			key_fields.append('"{}"'.format(self.Fields[i][-1]))

		value_fields = []
		for i in self.KeyFields:
			value_fields.append('"{}"'.format(self.SpecialCharEncode(input_dict[i])))

		primary_key = self.DbFetchPrimaryKeyValue(input_dict)
		cursor = self.Connection.cursor()
		if self.DbIsRecordExisted(input_dict) is False:
			try:
				body = "insert into {0}({1}) values({2});".format(self.Table,
					self.ListToString(key_fields),
					self.ListToString(value_fields))
				cursor.execute(body)
				self.Connection.commit()
			except Exception as e:
				print '\tException on inserting records to {0}:\n\tError -> {1}'.format(self.Table, str(e))
				return False
			else:
				print '\tInserted {}'.format(primary_key)
				return True
		elif self.DbIsRecordExisted(input_dict) is True:
			for i in xrange(len(key_fields)):
				key = key_fields[i]
				value = value_fields[i]
				value_in_db = self.DbFetchKeyValue(key, primary_key)
				if value_in_db is None:
					continue
				if str(value).replace('"', '') != str(value_in_db):
					try:
						body = 'update {0} set {1}={2} where {3}="{4}";'.format(self.Table,
							key.replace('"', ''), value, self.Fields[self.PrimaryKey][-1], primary_key)
						cursor.execute(body)
						self.Connection.commit()
					except Exception as e:
						print '\tException on updating field {0} to {1}:\n\tError -> {2}'.format(key, value, str(e))
						print body
						return False
					else:
						print '\t[{2}] Updated {0}'.format(key, value, primary_key)
				# else:
				# 	print 'Skipped to update {0} to {1}'.format(key, value)
			return True

	def DbFetchPrimaryKeyValue(self, input_dict):
		return input_dict[self.PrimaryKey]

	def DbIsRecordExisted(self, input_dict):
		event_number = input_dict[self.PrimaryKey]
		try:
			cursor = self.Connection.cursor()
			cursor.execute('select count(*) from {} where "{}" = "{}";'.format(self.Table,
				self.Fields[self.PrimaryKey][-1], event_number))
		except:
			return None
		else:
			ret = cursor.fetchall()[0][0]
			if ret == 1:
				return True
			elif ret == 0:
				return False

	def DbFetchKeyValue(self, searchKey, primaryKeyValue):
		try:
			cursor = self.Connection.cursor()
			body = 'select {0} from {1} where {2} = "{3}";'.format(searchKey.replace('"', ''), self.Table,
				self.Fields[self.PrimaryKey][-1], primaryKeyValue)
			cursor.execute(body)
			return cursor.fetchall()[0][0]
		except:
			return None

	def SpecialCharEncode(self, data):
		ret = data.replace('"', '&quote;')
		return ret

	def SpecialCharDecode(self, data):
		ret = data.replace('&quote;', '"')
		return ret

	def ListToString(self, lst):
		return ','.join([i for i in lst])

	def SQLInterface(self, command):
		cursor = self.Connection.cursor()
		cursor.execute(command)
		cursor.fetchall()
		cursor.close()


database = 'D:\\iBackup\\PLI.db'

#	CS3500
a = PLIServer('CS3500')
b = SQLLiteServer(database=database, table='CS3500')
for i in a.Result:
	b.DbUpdate(i)

#	IOC_UVC
c = PLIServer('IOC_UVC')
d = SQLLiteServer(database=database, table='IOC_UVC')
for j in c.Result:
	d.DbUpdate(j)
