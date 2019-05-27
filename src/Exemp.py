# -*- coding: utf-8 -*-

"""
<entity name = "Duel">
	<field>
		<name>duel_id</name>
		<type>int</type>
		<noNULL>Y</noNULL>
		<primaryKey>Y</primaryKey>
		<note>id</note>
	</field>
	<field>
		<name>fighter_1</name>
		<type>int</type>
		<noNULL>Y</noNULL>
		<foreignKey>Y</foreignKey>
		<note>id</note>
	</field>
	<field>
		<name>fighter_2</name>
		<type>int</type>
		<noNULL>Y</noNULL>
		<foreignKey>Y</foreignKey>
		<note>id</note>
	</field>
	<field>
		<name>winner</name>
		<type>int</type>
		<note>id</note>
	</field>
	<function>
		<name>score</name>
		<type>string</type>
	</function>
	<function>
		<name>winner</name>
		<type>int</type>
	</function>
</entity>
"""