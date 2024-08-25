# Adieu, Adieu

import inflect


def main():
    """
    Prompts the user for names, one per line, until the user inputs
    control-d. Assume that the user will input at least one name. Then bid
    adieu to those names, separating two names with one `and`, three names
    with two commas and one `and`, and `n` names with `n - 1` commas and
    one and, as in the below:

    Adieu, adieu, to Liesl
    Adieu, adieu, to Liesl and Friedrich
    Adieu, adieu, to Liesl, Friedrich, and Louisa
    Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
    """

    try:
        names = []

        while True:
            names.append(input("Name: ").capitalize().strip())

    except EOFError:
        p = inflect.engine()

        print("\nAdieu, adieu, to", p.join(names))


if __name__ == "__main__":
    main()
