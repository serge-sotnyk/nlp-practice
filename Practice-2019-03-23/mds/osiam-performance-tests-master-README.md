# performance-tests [![Circle CI](https://circleci.com/gh/osiam/performance-tests.svg?style=svg)](https://circleci.com/gh/osiam/performance-tests)

The performance tests for OSIAM

## Install

You can run the performance-tests on your machine, you only need to install
java, maven and docker, and configure docker.

The tests will fetch the snapshot dependencies from evolvis or you clone the
following repos and install them with `mvn clean install`

```
https://github.com/osiam/scim-schema
https://github.com/osiam/connector4java
https://github.com/osiam/osiam
```

### Configure Docker

The performance-tests use the [docker-maven-plugin]
(https://github.com/alexec/docker-maven-plugin), which utilizes [docker-java]
(https://github.com/docker-java/docker-java). In order to run the
performance-tests, you need to ensure that your docker daemon listens on the
TCP port `2375`.

How exactly this works depends on your operating system, but

    echo 'DOCKER_OPTS="-H tcp://127.0.0.1:2375 -H unix:///var/run/docker.sock' >> /etc/default/docker

is a good starting point. For further information, please refer to the
[docker-java README](https://github.com/docker-java/docker-java#build-with-maven)
and the official Docker documentation.

## Run

To run the performance-tests against 

postgres (default)

    $ mvn clean verify

mysql

    $ mvn clean verify -P mysql

## Retrieving test results

The performance tests generate two files containing the test results:

* raw JMeter results (*.jtl) under `./target/jmeter/results`
* An HTML report under `./target/jmeter-reports`

## How to modify the test data

To change the amount of Users and Groups you can simply change the following
two variables in the class [TestDataCreation]
(https://github.com/osiam/performance-tests/blob/master/src/main/java/org/osiam/tests/performance/tools/TestDataCreation.java):

```
private static final int NUMBER_USER = 1000;
private static final int NUMBER_GROUPS = 50;
```
to the amount you need.

## How to add or extend tests

To extend or change the tests edit the corresponding Java source file and
re-run the performance-tests. To change the test plan issue the following
command:

    $ mvn package jmeter:gui

Then change the test plan as needed.

### Adding new tests

To add a new test create a new Java source file named after your new test that
extends `PerformanceTestContext` and add a `run()` method annotated with `@org.junit.Test`:

```
public class MyShinyNewPerformanceTest extends PerformanceTestContext {

    @org.junit.Test
    public void run(){
        [...]
    }
}
```

Then extend the JMeter test plan. Issue the command:

    $ mvn package jmeter:gui

Now open the [JMeter test plan (src/test/jmeter/OSIAM Performance Test.jmx)]
(https://github.com/osiam/performance-tests/blob/master/src/test/jmeter/OSIAM%20Performance%20Tests.jmx).

**Info:** To make sure that cache doesn't modify the test results we always run
a test a few time before the real time measuring starts. For this we add for
every Thread a dry run thread which runs 3 times.

In the JMeter GUI add a new Thread Group named after your test class. 

    Edit -> Add -> Threads(Users) -> Thread Group

In the Thread Group you can add a JUnit Request

right click on the Thread Group -> Add -> Sampler -> JUnit Request

Set the following Options:

Dry Run Thread: Loop Count = 3

Thread: Loop Count = 100

JUnit Requests:

* activate "Search for JUnit 4 annotations"
* In the Box classname: select/write the full name of your testclass
* activate: Append runtime exceptions

Make sure that the Threads setUp and tearDown are always the first and the last
Thread in the Testplan.

