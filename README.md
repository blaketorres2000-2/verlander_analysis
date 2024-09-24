# Verlander Analysis

## Overview

As a software developer, I strive to enhance my data analysis skills by exploring real-world datasets and applying statistical methods. This project focuses on analyzing the pitching performance of Justin Verlander in the 2019 and 2022 seasons. The goal is to examine the relationship between pitch type and count, and gain insights into Verlander’s pitching strategies in different situations.

The dataset contains details about each pitch thrown by Verlander, including the pitch type (fastball, slider, curveball, changeup), ball-strike count, release speed, and the outcome of each pitch. The data was sourced from [Baseball Savant](https://baseballsavant.mlb.com/), accessed through the baseballr package.

This software aims to answer key questions regarding Verlander’s pitching tendencies and how certain combinations of pitch types and counts are more or less frequent than expected under the assumption of independence. By writing this software, I further develop my statistical analysis and Python programming skills.

Software Demo Video: https://youtu.be/86IpgjDhF84

## Data Analysis Results

1. **Is Verlander's pitch type independent of the count in 2019 and 2022?**
   - 2019: Pitch type is dependent on count (Chi-square test p-value < 0.05).
   - 2022: Pitch type is dependent on count (Chi-square test p-value < 0.05).

2. **Which combinations of pitch type and count appear more or fewer than expected under the assumption of independence?**
   - The analysis revealed combinations with both higher and lower-than-expected frequencies, with some pitch types (e.g., fastballs) thrown more often in specific counts and fewer in others.

3. **How does the average release speed vary by pitch type between 2019 and 2022?**
   - Fastball (FF) release speeds were consistently higher across both years, with slight variations in other pitch types.

4. **Which pitch is Justin Verlander most likely to throw for each pitch count and what is the expected speed for that pitch?**
   - For each pitch count, the analysis determined the pitch type that Verlander is most likely to throw and the average release speed for that pitch type.
   - Justin Verlander is almost always likely to throw a fastball. He threw more fastballs for every count than any other pitch. 
   - Also, his speed averages in the mid 95's. 

## Development Environment

- **Tools Used:** Visual Studio Code, GitHub
- **Programming Language:** Python
- **Libraries:** Pandas, Scipy, Numpy

## Useful Websites

* [Pandas Documentation](https://pandas.pydata.org/)
* [Scipy Documentation](https://docs.scipy.org/doc/scipy/)
* [Baseball Savant](https://baseballsavant.mlb.com/)
* [Kaggle](https://www.kaggle.com/datasets/mexwell/justin-verlander-pitches?select=verlander-pitches-2022.csv)

## Future Work

* Add analysis of pitch effectiveness based on outcomes (e.g., strikeouts, hits).
* Visualize the data using graphs and charts for better understanding.
* Explore other seasons or additional players for comparison.
