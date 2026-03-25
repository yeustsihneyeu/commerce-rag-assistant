def faq_select_k(scores: list[float]) -> int:
    if not scores:
        return 0

    if len(scores) < 3:
        return 1

    s1, s2, s3 = scores[:3]

    if s1 < 3:
        k = 1

    elif s1 < 6:
        k = 1

    else:
        if (s1 - s2) >= 2.5:
            k = 1
        elif s2 >= 5 and (s2 - s3) >= 1.5:
            k = 2
        else:
            k = 1
    return k
