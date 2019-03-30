# EvalExpr

# Trace:

# = Host-specific information ====================================================
$> hostname; uname -msr
e1r11p5.42.fr
Darwin 15.6.0 x86_64
$> date
Mon Jul 25 17:51:01 CEST 2016
$> gcc --version
	Configured with: --prefix=/Applications/Xcode.app/Contents/Developer/usr --with-gxx-include-dir=/usr/include/c++/4.2.1
Apple LLVM version 7.3.0 (clang-703.0.31)
	Target: x86_64-apple-darwin15.6.0
	Thread model: posix
	InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
	$> clang --version
Apple LLVM version 7.3.0 (clang-703.0.31)
	Target: x86_64-apple-darwin15.6.0
	Thread model: posix
	InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin

	= User files collection ========================================================
	Collecting user files from Vogsphere
	Repository URL: intra/2016/activities/piscine_c_evalexpr/rchiorea

	= Git history ==================================================================
	$> git -C /var/folders/4j/yp4n2j395p70ltr3c9mfnp8h0000gq/T/tmpFWtH3o/user log --pretty='%H - %an, %ad : %s'
	da86a408e1f339407c5aa46ca3fbb18b189be11d - Rares CHIOREANU, Sun Jul 24 12:24:15 2016 +0300 : update
	d981147df11f70a06f8cfe9cccea8d0987e53e33 - Rares CHIOREANU, Sun Jul 24 12:19:28 2016 +0300 : ok
	d7df72fcacbbe9cd134acb73653e26b82b1fdc83 - Rares CHIOREANU, Sun Jul 24 10:18:26 2016 +0300 : Eval Expr

	= Collected files ==========================================
	$> ls -lAR /var/folders/4j/yp4n2j395p70ltr3c9mfnp8h0000gq/T/tmpFWtH3o/user
	total 8
	-rw-r--r--   1 deepthought  deepthought  1251 Jul 25 17:51 __GIT_HISTORY
	drwxr-xr-x  11 deepthought  deepthought   374 Jul 25 17:51 ex00

	/var/folders/4j/yp4n2j395p70ltr3c9mfnp8h0000gq/T/tmpFWtH3o/user/ex00:
	total 72
	-rw-r--r--  1 deepthought  deepthought  1095 Jul 25 17:51 Makefile
	-rw-r--r--  1 deepthought  deepthought  1386 Jul 25 17:51 ft_eliminare.c
	-rw-r--r--  1 deepthought  deepthought  1223 Jul 25 17:51 ft_evalexpr.h
	-rw-r--r--  1 deepthought  deepthought  1100 Jul 25 17:51 ft_number.c
	-rw-r--r--  1 deepthought  deepthought  1292 Jul 25 17:51 ft_op_primar.c
	-rw-r--r--  1 deepthought  deepthought  1161 Jul 25 17:51 ft_op_secundar.c
	-rw-r--r--  1 deepthought  deepthought  1172 Jul 25 17:51 ft_putchar.c
	-rw-r--r--  1 deepthought  deepthought  1233 Jul 25 17:51 ft_verificare.c
	-rw-r--r--  1 deepthought  deepthought  1132 Jul 25 17:51 main.c

	= ex00 =========================================================================
	$> /usr/bin/norminette  ft_number.c ft_op_primar.c ft_evalexpr.h ft_op_secundar.c ft_verificare.c main.c ft_putchar.c ft_eliminare.c | grep -E '^(Error|Warning)'

	$> make && ls -la eval_expr
	gcc -c -Wall -Wextra -Werror *.c
	gcc -o eval_expr -Wall -Wextra -Werror *.o
	-rwxr-xr-x  1 deepthought  deepthought  9024 Jul 25 17:51 eval_expr

	= Test 1 ===================================================
	$> ./tjb8ykro0rgqwej3lrmr78bq "66 - 73"
	$> diff -U 3 user_output_test1 test1.output | cat -e

	Diff OK :D
	OK, incrementing grade by 5
	= Test 2 ===================================================
	$> ./tjz5tyhde8t9azt31b1bdbiw "50 - 45 * 14 % 2"
	$> diff -U 3 user_output_test2 test2.output | cat -e

	Diff OK :D
	OK, incrementing grade by 20
	= Test 3 ===================================================
	$> ./ymkw8vxttine5tn3ab371jqx "20 - 99 / (96 - 30 * (57 - 76) - 43 % 20) - 17"
	$> diff -U 3 user_output_test3 test3.output | cat -e

	Diff OK :D
	OK, incrementing grade by 10
	= Test 4 ===================================================
	$> ./f279mnml98ngp1jeiiq1sloo "0"
	$> diff -U 3 user_output_test4 test4.output | cat -e

	Diff OK :D
	OK, incrementing grade by 10
	= Test 5 ===================================================
	$> ./qtccr0uixbywm7f8v3xy5m36 "-93"
	$> diff -U 3 user_output_test5 test5.output | cat -e

	Diff OK :D
	OK, incrementing grade by 20
	= Test 6 ===================================================
	$> ./u6vo5oxvttdphji4o82t3ict "45-37"
	$> diff -U 3 user_output_test6 test6.output | cat -e

	Diff OK :D
	OK, incrementing grade by 10
	= Test 7 ===================================================
	$> ./9n2sz5w2zvhud3yv6nkod1jq "20+19*(13+59/(6+4)-97%11)-76"
	$> diff -U 3 user_output_test7 test7.output | cat -e

	Diff OK :D
	OK, incrementing grade by 10
	= Test 8 ===================================================
	$> ./ruztj2s11o6pqchq1vbshusu "86      -47            *(-26-75/(47-98/23)+17/(-         86  +          44*38))"
	$> diff -U 3 user_output_test8 test8.output | cat -e
	--- user_output_test8   2016-07-25 17:51:12.000000000 +0200$
	+++ test8.output        2016-07-25 17:51:12.000000000 +0200$
	@@ -1 +1 @@$
	-1355$
	+13058$

	Diff KO :(
			KO
			Grade: 85

			= Final grade: 85 ==============================================================

