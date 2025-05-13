import numpy
from lap_lengths import piastri_lap_lengths


def main():

    piastri_lap_lengths.sort()
    num_of_laps = len(piastri_lap_lengths)
    total_len_laps = sum(piastri_lap_lengths)

    # MEAN
    mean = total_len_laps/num_of_laps

    print(f"The mean of the laps is approximately {mean:.2f}")

    # MEDIAN
    median = numpy.quantile(piastri_lap_lengths, 0.5)

    print(f"The median of the laps is approximately {median:.2f}")

    # FIRST QUARTILE
    q1 = numpy.quantile(piastri_lap_lengths, 0.25)

    print(f"The first quartile of the laps is approximately {q1:.2f}")

    # THIRD QUARTILE
    q3 = numpy.quantile(piastri_lap_lengths, 0.75)

    print(f"The third quartile of the laps is approximately {q3:.2f}")

    # OUTLIERS
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = [laps for laps in piastri_lap_lengths if laps > upper_bound or laps < lower_bound]
    print(f"The laps which are outliers are: {outliers}")


if __name__ == "__main__":
    main()
