# Jest Circus Memory Leak

run `yarn test`

Result:

```
$ node --expose-gc ./node_modules/.bin/jest --logHeapUsage --runInBand funky
 PASS  tests/funky-36.test.js (20 MB heap size)
 PASS  tests/funky-86.test.js (22 MB heap size)
 PASS  tests/funky-28.test.js (24 MB heap size)
 PASS  tests/funky-35.test.js (26 MB heap size)
 PASS  tests/funky-85.test.js (28 MB heap size)
 PASS  tests/funky-16.test.js (30 MB heap size)
 PASS  tests/funky-82.test.js (32 MB heap size)
 PASS  tests/funky-74.test.js (34 MB heap size)
 PASS  tests/funky-60.test.js (36 MB heap size)
 PASS  tests/funky-88.test.js (39 MB heap size)
 PASS  tests/funky-79.test.js (41 MB heap size)
 PASS  tests/funky-40.test.js (43 MB heap size)
 PASS  tests/funky-22.test.js (45 MB heap size)
 PASS  tests/funky-68.test.js (47 MB heap size)
 PASS  tests/funky-80.test.js (49 MB heap size)
 PASS  tests/funky-34.test.js (51 MB heap size)
 PASS  tests/funky-29.test.js (53 MB heap size)
 PASS  tests/funky-57.test.js (55 MB heap size)
 PASS  tests/funky-67.test.js (57 MB heap size)
 PASS  tests/funky-47.test.js (59 MB heap size)
 PASS  tests/funky-33.test.js (61 MB heap size)
 PASS  tests/funky-92.test.js (63 MB heap size)
 PASS  tests/funky-71.test.js (65 MB heap size)
 PASS  tests/funky-43.test.js (67 MB heap size)
 PASS  tests/funky-98.test.js (69 MB heap size)
 PASS  tests/funky-93.test.js (71 MB heap size)
 PASS  tests/funky-91.test.js (73 MB heap size)
 PASS  tests/funky-62.test.js (75 MB heap size)
 PASS  tests/funky-69.test.js (77 MB heap size)
 PASS  tests/funky-59.test.js (79 MB heap size)
 PASS  tests/funky-94.test.js (81 MB heap size)
 PASS  tests/funky-75.test.js (83 MB heap size)
 PASS  tests/funky-46.test.js (85 MB heap size)
 PASS  tests/funky-23.test.js (87 MB heap size)
 PASS  tests/funky-15.test.js (89 MB heap size)
 PASS  tests/funky-41.test.js (91 MB heap size)
 PASS  tests/funky-31.test.js (94 MB heap size)
 PASS  tests/funky-38.test.js (96 MB heap size)
 PASS  tests/funky-37.test.js (98 MB heap size)
 PASS  tests/funky-65.test.js (100 MB heap size)
 PASS  tests/funky-81.test.js (102 MB heap size)
 PASS  tests/funky-18.test.js (104 MB heap size)
 PASS  tests/funky-97.test.js (106 MB heap size)
 PASS  tests/funky-87.test.js (108 MB heap size)
 PASS  tests/funky-89.test.js (110 MB heap size)
 PASS  tests/funky-20.test.js (112 MB heap size)
 PASS  tests/funky-53.test.js (114 MB heap size)
 PASS  tests/funky-11.test.js (116 MB heap size)
 PASS  tests/funky-58.test.js (118 MB heap size)
 PASS  tests/funky-76.test.js (120 MB heap size)
 PASS  tests/funky-99.test.js (122 MB heap size)
 PASS  tests/funky-49.test.js (124 MB heap size)
 PASS  tests/funky-84.test.js (126 MB heap size)
 PASS  tests/funky-70.test.js (128 MB heap size)
 PASS  tests/funky-72.test.js (130 MB heap size)
 PASS  tests/funky-66.test.js (132 MB heap size)
 PASS  tests/funky-83.test.js (134 MB heap size)
 PASS  tests/funky-42.test.js (136 MB heap size)
 PASS  tests/funky-12.test.js (138 MB heap size)
 PASS  tests/funky-21.test.js (140 MB heap size)
 PASS  tests/funky-10.test.js (142 MB heap size)
 PASS  tests/funky-17.test.js (144 MB heap size)
 PASS  tests/funky-61.test.js (146 MB heap size)
 PASS  tests/funky-77.test.js (148 MB heap size)
 PASS  tests/funky-32.test.js (150 MB heap size)
 PASS  tests/funky-96.test.js (152 MB heap size)
 PASS  tests/funky-25.test.js (154 MB heap size)
 PASS  tests/funky-54.test.js (156 MB heap size)
 PASS  tests/funky-45.test.js (158 MB heap size)
 PASS  tests/funky-63.test.js (160 MB heap size)
 PASS  tests/funky-78.test.js (162 MB heap size)
 PASS  tests/funky-27.test.js (165 MB heap size)
 PASS  tests/funky-39.test.js (167 MB heap size)
 PASS  tests/funky-50.test.js (169 MB heap size)
 PASS  tests/funky-13.test.js (171 MB heap size)
 PASS  tests/funky-19.test.js (173 MB heap size)
 PASS  tests/funky-73.test.js (175 MB heap size)
 PASS  tests/funky-48.test.js (177 MB heap size)
 PASS  tests/funky-95.test.js (179 MB heap size)
 PASS  tests/funky-44.test.js (181 MB heap size)
 PASS  tests/funky-90.test.js (183 MB heap size)
 PASS  tests/funky-64.test.js (185 MB heap size)
 PASS  tests/funky-14.test.js (187 MB heap size)
 PASS  tests/funky-55.test.js (189 MB heap size)
 PASS  tests/funky-51.test.js (191 MB heap size)
 PASS  tests/funky-26.test.js (193 MB heap size)
 PASS  tests/funky-56.test.js (195 MB heap size)
 PASS  tests/funky-24.test.js (197 MB heap size)
 PASS  tests/funky-30.test.js (199 MB heap size)
 PASS  tests/funky-52.test.js (201 MB heap size)
```

Comment out `testRunner: require.resolve('jest-circus/runner'),` in `jest.config.js`.

Result:

```
$ node --expose-gc ./node_modules/.bin/jest --logHeapUsage --runInBand funky
 PASS  tests/funky-36.test.js (17 MB heap size)
 PASS  tests/funky-40.test.js (17 MB heap size)
 PASS  tests/funky-28.test.js (17 MB heap size)
 PASS  tests/funky-79.test.js (16 MB heap size)
 PASS  tests/funky-35.test.js (16 MB heap size)
 PASS  tests/funky-16.test.js (16 MB heap size)
 PASS  tests/funky-88.test.js (17 MB heap size)
 PASS  tests/funky-86.test.js (17 MB heap size)
 PASS  tests/funky-34.test.js (17 MB heap size)
 PASS  tests/funky-74.test.js (17 MB heap size)
 PASS  tests/funky-85.test.js (17 MB heap size)
 PASS  tests/funky-29.test.js (17 MB heap size)
 PASS  tests/funky-22.test.js (17 MB heap size)
 PASS  tests/funky-60.test.js (17 MB heap size)
 PASS  tests/funky-80.test.js (17 MB heap size)
 PASS  tests/funky-57.test.js (17 MB heap size)
 PASS  tests/funky-82.test.js (17 MB heap size)
 PASS  tests/funky-68.test.js (17 MB heap size)
 PASS  tests/funky-59.test.js (17 MB heap size)
 PASS  tests/funky-26.test.js (17 MB heap size)
 PASS  tests/funky-52.test.js (17 MB heap size)
 PASS  tests/funky-25.test.js (17 MB heap size)
 PASS  tests/funky-17.test.js (17 MB heap size)
 PASS  tests/funky-51.test.js (17 MB heap size)
 PASS  tests/funky-10.test.js (17 MB heap size)
 PASS  tests/funky-48.test.js (17 MB heap size)
 PASS  tests/funky-70.test.js (17 MB heap size)
 PASS  tests/funky-81.test.js (17 MB heap size)
 PASS  tests/funky-95.test.js (17 MB heap size)
 PASS  tests/funky-67.test.js (17 MB heap size)
 PASS  tests/funky-24.test.js (17 MB heap size)
 PASS  tests/funky-78.test.js (17 MB heap size)
 PASS  tests/funky-55.test.js (17 MB heap size)
 PASS  tests/funky-30.test.js (17 MB heap size)
 PASS  tests/funky-71.test.js (17 MB heap size)
 PASS  tests/funky-75.test.js (17 MB heap size)
 PASS  tests/funky-69.test.js (17 MB heap size)
 PASS  tests/funky-64.test.js (17 MB heap size)
 PASS  tests/funky-21.test.js (17 MB heap size)
 PASS  tests/funky-99.test.js (17 MB heap size)
 PASS  tests/funky-27.test.js (17 MB heap size)
 PASS  tests/funky-44.test.js (17 MB heap size)
 PASS  tests/funky-98.test.js (17 MB heap size)
 PASS  tests/funky-96.test.js (17 MB heap size)
 PASS  tests/funky-11.test.js (17 MB heap size)
 PASS  tests/funky-13.test.js (17 MB heap size)
 PASS  tests/funky-38.test.js (17 MB heap size)
 PASS  tests/funky-56.test.js (17 MB heap size)
 PASS  tests/funky-14.test.js (17 MB heap size)
 PASS  tests/funky-20.test.js (19 MB heap size)
 PASS  tests/funky-19.test.js (17 MB heap size)
 PASS  tests/funky-41.test.js (17 MB heap size)
 PASS  tests/funky-62.test.js (17 MB heap size)
 PASS  tests/funky-83.test.js (17 MB heap size)
 PASS  tests/funky-33.test.js (17 MB heap size)
 PASS  tests/funky-73.test.js (17 MB heap size)
 PASS  tests/funky-92.test.js (17 MB heap size)
 PASS  tests/funky-49.test.js (17 MB heap size)
 PASS  tests/funky-53.test.js (17 MB heap size)
 PASS  tests/funky-91.test.js (17 MB heap size)
 PASS  tests/funky-43.test.js (17 MB heap size)
 PASS  tests/funky-76.test.js (17 MB heap size)
 PASS  tests/funky-23.test.js (17 MB heap size)
 PASS  tests/funky-42.test.js (17 MB heap size)
 PASS  tests/funky-90.test.js (17 MB heap size)
 PASS  tests/funky-93.test.js (17 MB heap size)
 PASS  tests/funky-45.test.js (17 MB heap size)
 PASS  tests/funky-37.test.js (17 MB heap size)
 PASS  tests/funky-65.test.js (17 MB heap size)
 PASS  tests/funky-47.test.js (17 MB heap size)
 PASS  tests/funky-32.test.js (17 MB heap size)
 PASS  tests/funky-72.test.js (17 MB heap size)
 PASS  tests/funky-94.test.js (17 MB heap size)
 PASS  tests/funky-15.test.js (17 MB heap size)
 PASS  tests/funky-54.test.js (17 MB heap size)
 PASS  tests/funky-50.test.js (17 MB heap size)
 PASS  tests/funky-77.test.js (17 MB heap size)
 PASS  tests/funky-12.test.js (17 MB heap size)
 PASS  tests/funky-84.test.js (17 MB heap size)
 PASS  tests/funky-46.test.js (17 MB heap size)
 PASS  tests/funky-31.test.js (17 MB heap size)
 PASS  tests/funky-61.test.js (17 MB heap size)
 PASS  tests/funky-66.test.js (17 MB heap size)
 PASS  tests/funky-63.test.js (17 MB heap size)
 PASS  tests/funky-39.test.js (17 MB heap size)
 PASS  tests/funky-58.test.js (17 MB heap size)
 PASS  tests/funky-97.test.js (17 MB heap size)
 PASS  tests/funky-18.test.js (17 MB heap size)
 PASS  tests/funky-87.test.js (17 MB heap size)
 PASS  tests/funky-89.test.js (17 MB heap size)
```

