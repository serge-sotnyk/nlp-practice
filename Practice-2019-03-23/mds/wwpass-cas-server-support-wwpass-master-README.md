cas-server-support-wwpass
========================

This module allows you to integrate [WWPass Authentication](https://www.wwpass.com/) into [JASIG CAS Single Sign-On Server](http://jasig.github.io/cas/4.0.0/index.html). 


NOTE: The distribution consists of two parts - the support module itself and an example application. For the example app to operate properly we bring specific CAS configuration based on MySQL user data tables. Due to CAS architecture and source-based nature some MySQL modules should be compiled in when creating CAS.war file. 




Installation & Configuration
============================

### Create a WWPass Developer Account
Signup for a free account on [WWPass developers website](https://developers.wwpass.com/) and follow the [getting started](https://developers.wwpass.com/documentation) instructions to obtain WWPass authorization credentials (WWPass certificate file and a private key file) for your CAS server: . 

### Build the server extension

``` bat
cd cas-server-support-wwpass
mvn clean package install
```


### Use the Maven Overlay Method to configure CAS


Follow the instructions in [http://jasig.github.io/cas/4.0.0/installation/Maven-Overlay-Installation.html](http://jasig.github.io/cas/4.0.0/installation/Maven-Overlay-Installation.html) and download the template [https://github.com/UniconLabs/simple-cas4-overlay-template](https://github.com/UniconLabs/simple-cas4-overlay-template)



### Quick configuration

CAS server behaviour depends on a set of configuration files - compilation-time and run-time

**cas-server-support-wwpass** distribution comes with a ready-made set of files, which produce demo CAS server working with our example app.

You will find the files in `cas-server-support-wwpass/overlay-extra` directory.

Copying instructions:

``` xml
#!/bin/sh

CFG_SRC="cas-server-support-wwpass/overlay-extra"
CFG_DEST="simple-cas4-overlay-template-master"

cp $CFG_SRC/resources/default_views.properties $CFG_DEST/src/main/resources/
cp $CFG_SRC/webapp/WEB-INF/view/jsp/default/ui/wwpassCasLoginView.jsp $CFG_DEST/src/main/webapp/WEB-INF/view/jsp/default/ui/
cp $CFG_SRC/webapp/WEB-INF/login-webflow.xml $CFG_DEST/src/main/webapp/WEB-INF/
cp $CFG_SRC/webapp/WEB-INF/deployerConfigContext.xml $CFG_DEST/src/main/webapp/WEB-INF/

cp -r $CFG_SRC/webapp/css $CFG_DEST/src/main/webapp/
cp -r $CFG_SRC/webapp/images $CFG_DEST/src/main/webapp/

cp $CFG_SRC/pom.xml $CFG_DEST/

cp $CFG_SRC/cas.properties /etc/cas/

# NOTE: next file comes from simple-cas4-overlay-template:

cp $CFG_DEST/etc/log4j.xml /etc/cas/


```


Edit WWPass settings in /etc/cas/cas.properties - registered SP name and paths to certificate and private key files:

```
# WWPass Settings
wwpass.certPath=/etc/ssl/certs/your_site.crt
wwpass.keyPath=/etc/ssl/certs/your_site.key

wwpass.sp.name=your_site_name
```
Now use `cas-server-support-wwpass/overlay-extra/sample-schema.sql` file to create the example user MySQL database 


Finally compile CAS.war:

``` bat
cd simple-cas4-overlay-template-master
mvn clean package install
```

You are done


### Compiling Example CAS client


Goto **cas-example** directory provided with **cas-server-support-wwpass** and compile it as usually

``` bat
cd cas-example
mvn clean package install
```

The directory has its own Readme.md file with instructions.

The example app shares the MySQL user database with CAS server. 
Use `cas-server-support-wwpass/overlay-extra/sample-schema.sql` file to create the database.


### Configuration details  

NOTE: some parts of configuration files correspond to particular MySQL-based example. 
You will rather use your own user catalog. This MySQL configuration is just easy-to-understand example.



#### pom.xml


Add the following block to the `pom.xml` in CAS overlay directory:

``` xml
    <dependency>
      <groupId>com.wwpass</groupId>
      <artifactId>cas-server-support-wwpass</artifactId>
      <version>0.1</version>
    </dependency>
```

Modify **build** section as follows:
``` xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>2.3</version>
                <configuration>
                    <warName>cas</warName>
                    <overlays>
                        <overlay>
                            <groupId>org.jasig.cas</groupId>
                            <artifactId>cas-server-webapp</artifactId>
                            <excludes>
                                <exclude>WEB-INF/cas.properties</exclude>
                                <exclude>WEB-INF/classes/log4j.xml</exclude>
                                <exclude>WEB-INF/deployerConfigContext.xml</exclude>
                                <exclude>WEB-INF/login-webflow.xml</exclude>
                                <exclude>WEB-INF/classes/default_views.properties</exclude>
                            </excludes>
                        </overlay>
                    </overlays>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.1</version>
                <configuration>
                    <source>1.7</source>
                    <target>1.7</target>
                </configuration>
            </plugin>
        </plugins>
        <finalName>cas</finalName>
    </build>
```

#### deployerConfigContext.xml
First, copy `deployerConfigContext.xml` from `cas-server-support-wwpass/overlay-extra` to `_cas_overlay_folder_/src/main/webapp/WEB-INF/`.
Also you can use default `deployerConfigContext.xml` file, for example, from CAS distribution (`cas-server-webapp/src/main/webapp/WEB-INF/deployerConfigContext.xml`). After you copy it to you overlay, follow the instructions bellow:

* add the `WwpassAuthenticationHandler` bean to the list of authentication handlers in `deployerConfigContext.xml`:

``` xml
    <bean id="authenticationManager" class="org.jasig.cas.authentication.PolicyBasedAuthenticationManager">
    
        <constructor-arg>
            <map>
                <entry key-ref="dbAuthHandler" value-ref="usernamePasswordCredentialsResolver"/>
                <entry key-ref="wwpassAuthenticationHandler" >
                    <null/>
                </entry>
            </map>
        </constructor-arg>
        
        <property name="authenticationPolicy">
            <bean class="org.jasig.cas.authentication.AnyAuthenticationPolicy"/>
        </property>
    </bean>
```

``` xml
    <bean id="wwpassAuthenticationHandler"
          class="com.wwpass.cas.support.authentication.handler.WwpassAuthenticationHandler">
        <property name="wwpassConnection" ref="wwpassConnection"/>
        <property name="wwpassDAO" ref="jdbcWwpassDAO"/>
    </bean>

    <bean name="wwpassConnection" class="com.wwpass.connection.WWPassConnection">
        <constructor-arg name="certFile" value="${wwpass.certPath}"/>
        <constructor-arg name="keyFile" value="${wwpass.keyPath}"/>
    </bean>

    <bean id="jdbcWwpassDAO"
          class="com.wwpass.cas.support.dao.JdbcWwpassDao">
        <property name="dataSource" ref="dataSource"/>    
    </bean>
```

- **wwpassConnection** = A bean represents library, which allows to authenticate user via WWPass.
- **jdbcWwpassDao** - A JDBC-based user servise, which implements interface WwpassDAO. You can write your own implementation of this interface, for example, getting user's principal from LDAP by WWPass PUID (`PUID - user/service_provider unique identifier`).


* if you decide to use JDBC-based user storage, you'll also need to add `dataSource` bean, for example, using `c3p0` library:

``` xml
    <bean id="dataSource"
          class="com.mchange.v2.c3p0.ComboPooledDataSource"
          p:driverClass="${database.driverClass}"
          p:jdbcUrl="${database.url}"
          p:user="${database.user}"
          p:password="${database.password}"
          p:initialPoolSize="${database.pool.minSize}"
          p:minPoolSize="${database.pool.minSize}"
          p:maxPoolSize="${database.pool.maxSize}"
          p:maxIdleTimeExcessConnections="${database.pool.maxIdleTime}"
          p:checkoutTimeout="${database.pool.maxWait}"
          p:acquireIncrement="${database.pool.acquireIncrement}"
          p:acquireRetryAttempts="${database.pool.acquireRetryAttempts}"
          p:acquireRetryDelay="${database.pool.acquireRetryDelay}"
          p:idleConnectionTestPeriod="${database.pool.idleConnectionTestPeriod}"
          p:preferredTestQuery="${database.pool.connectionHealthQuery}" />
```
then add **c3p0** dependency to `pom.xml` in CAS overlay directory:
``` xml
    <dependency>
        <groupId>c3p0</groupId>
        <artifactId>c3p0</artifactId>
        <version>0.9.1.2</version>
    </dependency>
```
and JDBC driver dependency for database type you are using, for example, MySQL:
``` xml
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>5.1.6</version>
    </dependency>
```



By default `JdbcWwpassDao` uses SQL schema described in file `cas-server-support-wwpass/overlay-extra/sample-schema.sql` to get **username** by **PUID**, but you can change query by setting up the **usernameByPuidQuery** property.


#### /etc/cas/cas.properties

To keep confidential information out of the XML config files, the configuration data should be saved in `cas.properties` file:

> Note, that by default this file must be on the path "/etc/cas/cas.properties", it is suitable for Linux systems. But if using Windows, you can change this setting in file "_cas_overlay_directory_/src/webapp/WEB-INF/spring-configuration/propertyFileConfigurer.xml"

``` properties
# == WWPass Settings ==

# Your Service Provider's certificate and key paths
wwpass.certPath=/etc/ssl/certs/example.com.crt
wwpass.keyPath=/etc/ssl/certs/example.com.key

# Service Provider's name on which the certificate was issued
wwpass.sp.name=example.com


# == Basic database connection pool configuration ==
database.driverClass=com.mysql.jdbc.Driver
database.url=jdbc:mysql://127.0.0.1/wwpass_cas
database.user=cas
database.password=changeit
database.pool.minSize=6
database.pool.maxSize=18
 
# Maximum amount of time to wait in ms for a connection to become
# available when the pool is exhausted
database.pool.maxWait=10000
 
# Amount of time in seconds after which idle connections
# in excess of minimum size are pruned.
database.pool.maxIdleTime=120
 
# Number of connections to obtain on pool exhaustion condition.
# The maximum pool size is always respected when acquiring
# new connections.
database.pool.acquireIncrement=6
 
# == Connection testing settings ==
 
# Period in s at which a health query will be issued on idle
# connections to determine connection liveliness.
database.pool.idleConnectionTestPeriod=30
 
# Query executed periodically to test health
database.pool.connectionHealthQuery=select 1
 
# == Database recovery settings ==
 
# Number of times to retry acquiring a _new_ connection
# when an error is encountered during acquisition.
database.pool.acquireRetryAttempts=5
 
# Amount of time in ms to wait between successive aquire retry attempts.
database.pool.acquireRetryDelay=2000
```
___


#### default_views.properties

To authenticate with WWPass, you'll need to add one new view - `wwpassCasLoginView`.  
Add the following lines to the end of properties file for your theme(s) or `default_views.properties` if you are using the default CAS theme.

``` properties
### WWPass Login view
wwpassCasLoginView.(class)=org.springframework.web.servlet.view.JstlView
wwpassCasLoginView.url=/WEB-INF/view/jsp/default/ui/wwpassCasLoginView.jsp
```


___
#### login-webflow.xml
The final step is to modify the login webflow to display the WWPass login view instead of original CAS login view. 

Simply replace `viewLoginForm` **view-state**:

``` xml
    <view-state id="viewLoginForm" view="wwpassCasLoginView" model="wwpassExtentedCredentials">
        <binder>
            <binding property="ticket" />
            <binding property="username" />
            <binding property="password" />
        </binder>
        <on-entry>
            <set name="viewScope.commandName" value="'wwpassExtentedCredentials'" />
            <set name="viewScope.wwpassCommandName" value="'wwpassExtentedCredentials'" />
            <set name="viewScope.spName" value="'SDK%20Test'" />
        </on-entry>
        <transition on="submit" bind="true" validate="true" to="realSubmit">
            <evaluate expression="authenticationViaFormAction.doBind(flowRequestContext, flowScope.wwpassExtentedCredentials)" />
        </transition>
    </view-state>
    
```
`credential` **var** replace with:
``` xml
    <var name="wwpassExtentedCredentials" class="com.wwpass.cas.support.authentication.credential.WwpassWithUsernamePasswordCredentials" />
```

And `realSubmit` **action-state** replace with:
``` xml
  <action-state id="realSubmit">
    <evaluate expression="authenticationViaFormAction.submit(flowRequestContext, flowScope.wwpassExtentedCredentials, messageContext)" />
    <transition on="warn" to="warn" />
    <transition on="success" to="sendTicketGrantingTicket" />
    <transition on="successWithWarnings" to="showMessages" />
    <transition on="authenticationFailure" to="handleAuthenticationFailure" />
    <transition on="error" to="generateLoginTicket" />
  </action-state>
```


