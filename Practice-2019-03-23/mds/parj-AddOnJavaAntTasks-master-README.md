![Build Status](https://travis-ci.org/parj/AddOnJavaAntTasks.png)

[![DepShield Badge](https://depshield.sonatype.org/badges/parj/AddOnJavaAntTasks/depshield.svg)](https://depshield.github.io)

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fparj%2FAddOnJavaAntTasks.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fparj%2FAddOnJavaAntTasks?ref=badge_large)

# Gradle method

    apply plugin : 'addonjavaanttasks'

    buildscript {
       repositories {
          mavenCentral()
       }
       dependencies {
          classpath group: 'uk.co.firstzero', name: 'AddOnJavaAntTasks', version: '2.8'
       }
    }


## CSV To Excel
Converts a set of csv files into 1 Excel file. Each csv file is a sheet within excel

    csvToExcelArgs {
    	inputFiles = fileTree(dir: 'src/test/resources/csv/CsvToExcel', include: 'output.csv')
    	outputFile = 'src/test/resources/csv/CsvToExcel/report.xls'
    	separator = ','
    }

Run `gradle csvToExcelTask`

## CSV Diff
Diffs two directories containing csv files. Each directory must have the same name and number of files as the other

    csvDiffArgs {
    	resultDirectory = projectDir.toString() + "/src/test/resources/csv/CsvDiff";
    	separator = ","
    	controlDirectory = fileTree(dir: 'src/test/resources/csv/CsvDiff/control', include: '*.csv')
    	testDirectory = 'src/test/resources/csv/CsvDiff/test'
    	keyColumns = 'Header_1;Header_3'
    }

Run `gradle csvDiffTask`

## XML Clean
Strips out fluff from the XML and manipulating the XML. The use case for this is, before comparison, sometimes XMLs need to be cleaned and renamed. The cleaned xmls can be diffed using xmlunittask.

    xmlCleanArgs {
    	inputDirectory = fileTree(dir: 'src/test/resources/xml/AntXPathTest', include: '*.xml')
    	outputDirectory = 'src/test/resources/xml/AntXPathTest'
    	renamePattern = '//publish_date[position() = 1]#_#//price[position() = 1]'
    	modifyPaths = [ new uk.co.firstzero.xml.ModifyPath(path: "//title", delete:"True"),
    					new uk.co.firstzero.xml.ModifyPath(path: "//author", value:"ToDo")]
    }

Run `gradle xmlCleanTask`

## XML DIFF
Diffs two directories containing xml files. Each directory must have the same name and number of files as the other

    xmlUnitArgs {
    	resultDirectory = projectDir.toString() + "/src/test/resources/xml/AntXMLUnitTest";
    	separator = ","
    	controlDirectory = fileTree(dir: 'src/test/resources/xml/AntXMLUnitTest/control', include: '*.xml')
    	testDirectory = 'src/test/resources/xml/AntXMLUnitTest/test'
    }

Run `gradle xmlUnitTask`

## READ BLOB
Extracts Blobs from Database.SQL should contain a string name and then blob

    readBlobArgs {
        className = "org.h2.Driver"
        String databaseLocation = projectDir.toString() + "/src/test/resources/sql/test"
        jdbcUrl = "jdbc:h2:" + databaseLocation + ";IFEXISTS=TRUE"
        user = "sa"
        password = ""
        extension = ".jpg"
        sql = "SELECT name, blob from TEST"
        outputDirectory = "build/tmp"
        unzip = true
    }

Run `gradle readBlobTask`

## WEBDAV PULL
Downloads files from a WEBDAV site, proxy configuration is supported

    pullArgs {
        user = 'admin'
        password = "admin"
        url = "http://localhost:8080/repository/default"
        file = "output.csv"
        outFile = "src/test/resources/webdav/output.csv"
        overwrite = true
        //proxyUser = user
        //proxyPassword = password
        //proxyHost = abcd.test
        //proxyPort = 1234
    }

Run `gradle pullTask`

## WEBDAV PUSH
Pushes files to a WEBDAV site, proxy configuration is supported

    pushArgs {
        user = 'admin'
        password = "admin"
        url = "http://localhost:8080/repository/default"
        overwrite = true
        tree = fileTree(dir: 'src/test/resources/webdav', include: '*.csv')
        createDirectoryStructure = false
    	//proxyUser = user
        //proxyPassword = password
        //proxyHost = abcd.test
        //proxyPort = 1234
    }

Run `gradle pushTask`

# Using AddOnJavaAntTasks on ANT
Ensure you have downloaded the *anttasks jar* and placed that in your $ANT_HOME/lib. The jar is available from http://goo.gl/CWv92n

# Addon Ant Tasks
* AntDav - To upload and download from WebDav Servers
* AntCsvtoExcel - To convert a set of csv files into 1 Excel file. Each csv file is a sheet within
* AntXMLUnit - To compare two directory of xml files using XMLUnit and produce a csv file report for each
* AntXPath - For modifying xml files using xpaths, sometimes for comparison you want to physically strip out timestamp elements, etc. AntXPath is capable of doing that.
* AntReadBlob - For bulk reading and downloading files from the database

## AntDav

> Requires JackRabbit Stand Alone jar - http://jackrabbit.apache.org/downloads.html if you are doing development and would like to run the unit tests.

### Getting Started
In your ant build.xml declare the custom tasks:

    <taskdef name="pull" classname="uk.co.firstzero.webdav.Pull" />
    <taskdef name="push" classname="uk.co.firstzero.webdav.Push" />

### Task Examples
    <!-- Example of pushing file(s) to webdav -->
    <push url="http://localhost:9090/repository/default"
          user="admin"
          password="admin"
          overwrite="true">
          <fileset dir="." includes="README"/>
    </push>

    <!-- Example of pulling files from webdav -->
    <pull url="http://localhost:9090/repository/default"
          user="admin"
          password="admin"
          file="README"
          overwrite="true"/>
    </pull>

## AntCsvToExcel

> Requires JExcelApi - http://sourceforge.net/projects/jexcelapi/files/jexcelapi/2.6.12/jexcelapi_2_6_12.zip/download

### Getting Started
    <target name="declare-tasks">		
        <!-- Dependency on JExcelApi -
         http://sourceforge.net/projects/jexcelapi/files/jexcelapi/2.6.12/jexcelapi_2_6_12.zip/download
	    -->
		<taskdef name="csvToexcel" classname="uk.co.firstzero.csv.AntCsvToExcel" />
    </target>

### Task Examples
	<!-- Example of combining csv files to an excel file -->
	<target name="csvToexcel" depends="declare-tasks">
		<csvToexcel outputFile="report.xls" separator=",">
			<fileset dir="." includes="*.csv"/>
		</csvToexcel>
	</target>

## AntXMLUnit

Ensure you have downloaded the *AntCsvToExcel jar* and placed that in your $ANT_HOME/lib

> Requires XMLUnit (xmlunit-bin) - http://sourceforge.net/projects/xmlunit/files/xmlunit%20for%20Java/XMLUnit%20for%20Java%201.3/

### Getting Started
    <target name="declare-tasks">
        <taskdef name="diffxml" classname="uk.co.firstzero.xml.AntXMLUnit"/>
    </target>

### Task Examples

    <target name="diff" depends="jar, declare-tasks">
        <diffxml testDirectory="2" resultDirectory="." verbose="True">
            <fileset dir="1" includes="*.xml"/>
        </diffxml>
    </target>

## AntXPath

> Requires XALAN (for JAVA 1.4 and below, JAVA 1.5 and above nothing is required) - http://xml.apache.org/xalan-j/downloads.html#latest-release

### Getting Started
    <target name="declare-tasks">
        <taskdef name="xpath" classname="uk.co.firstzero.xml.AntXPath"/>
        <taskdef name="modifyPath" classname="uk.co.firstzero.xml.ModifyPath"/>
    </target>

### Task Examples
Rename Pattern - Is the pattern in which the files you should be renamed - The value is picked up from the xml using xpaths. This makes sense, when you remove/change values, rename the files and then do a comparison


    <target name="modify" depends="jar, declare-tasks">
       <xpath outputDirectory="out"
	      renamePattern="//publish_date[position() = 1]#_#//price[position() = 1]"
	      verbose="True">
            <fileset dir="." includes="input.xml"/>
	        <modifyPath path="//title" delete="True"/>
	        <modifyPath path="//author" value="ToTo"/>
       </xpath>
    </target>

## AntReadBlob

> Requires the dependencies jar of the Database you are connecting to

### Getting Started
    <target name="declare-tasks">
        <taskdef name="readBlob" classname="uk.co.firstzero.sql.AntReadBlob"/>
    </target>

### Task Examples
Rename Pattern - Is the pattern in which the files you should be renamed - The value is picked up from the xml using xpaths. This makes sense, when you remove/change values, rename the files and then do a comparison

    <target name="readBlob" depends="jar, declare-tasks">
       <readBlob className="out"
	      jdbcUrl="jdbc:h2:src/test/resources/sql/test;IFEXISTS=TRUE"
	      user="sa" password="" extension=".jpg"
          sql="SELECT name, blob from TEST"
          outputDirectory="build/tmp" unzip="True">
       </readBlob>
    </target>

