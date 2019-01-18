###############################################################################
# DONE:  READ the code below. TRACE (by hand) the execution of the code,
# predicting what will get printed.  Then run the code
# and compare your prediction to what actually was printed.
# Then mark this _TODO_ as DONE and commit-and-push your work.
#
###############################################################################


def main():
    hello("Snow White")
    goodbye("Bashful")
    hello("Grumpy")
    hello("Sleepy")
    hello_and_goodbye("Magic Mirror", "Cruel Queen")


def hello(friend):
    print("Hello,", friend, "- how are things?")


def goodbye(friend):
    print("Goodbye,", friend, '- see you later!')
    print('   Ciao!')
    print('   Bai bai!')


def hello_and_goodbye(person1, person2):
    hello(person1)
    goodbye(person2)


main()
##########################################
# Prediction:
# hello, Snow White, -how are things?
# Goodbye, Bashful, -see you later!
# Ciao!
# Bai bai!
# hello, Grumpy, -how are things?
# hello, Sleepy, -how are things?
# hello, Magic Mirror, -how are things?
# Goodbye, Cruel Queen, -see you later!
# Ciao!
# Bai bai!
#
##########################################