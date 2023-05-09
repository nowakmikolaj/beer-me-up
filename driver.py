import sys

from pyke import knowledge_engine
from pyke import krb_traceback


def run_driver():
    engine = knowledge_engine.engine(__file__)
    engine.reset()

    engine.activate('rules')

    print("doing proof")

    try:
        with engine.prove_goal(
                'rules.beer($beer)') as gen:  # STUDENTS: you will need to edit this line
            for vars, plan in gen:
                # STUDENTS: you will need to edit this line
                print("You should drink: %s" % (vars['beer']))

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    run_driver()
