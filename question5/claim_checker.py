from rag_engine import get_answer

def check_claim(
        illness,
        policy_months):

    query=f"""

Customer Scenario

Illness: {illness}

Policy Active:
{policy_months} months

Check:

1 Covered or not
2 Waiting period completed
3 Required documents
4 Chances of approval
5 Final recommendation

"""

    result=get_answer(query)

    return result