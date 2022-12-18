import random
import numpy as np
from scipy import stats

random.seed(42)

# 正規母集団Dのパラメータ
mean = 0
var = 1

est_means_list = []
est_vars_list = []

# サンプルの個数は10個と100個
for sample_num in [10, 100]:
    print(f'サンプルの個数：{sample_num}')

    # サンプルの集合
    S = np.array([[random.gauss(mean, var) for i in range(sample_num)] for j in range(100)])

    # カウント変数
    count_mean, count_var = 0, 0
    diff_mean_sum, diff_var_sum = 0, 0
    est_means, est_vars = [], []

    # 各Siについて
    for s in S:
        # 平均と分散の推定量を計算する
        est_mean = s.mean()
        est_var = s.var(ddof=1)
        est_means.append(est_mean)
        est_vars.append(est_var)

        # 母平均と標本平均の差を求める
        diff_mean = abs(mean - est_mean)
        diff_var = abs(var - est_var)
        diff_mean_sum += diff_mean
        diff_var_sum += diff_var

        # 平均の95%信頼区間の計算
        # 統計量tを求める
        t_mean = (est_mean - mean)/np.sqrt(est_var/len(s))
        # t分布の上側2.5%点を求める（自由度はsample_num-1）
        t_upper = stats.t.ppf(0.975, len(s)-1)
        # 信頼区間の計算
        interval_mean_min = est_mean - t_upper * np.sqrt(est_var/len(s))
        interval_mean_max = est_mean + t_upper * np.sqrt(est_var/len(s))

        # カイ二乗分布の上側2.5%点と上側2.5%点を求める（自由度はsample_num-1）
        chi2_lower = stats.chi2.ppf(0.025, len(s)-1)
        chi2_upper = stats.chi2.ppf(0.975, len(s)-1)
        # 信頼区間の計算
        interval_var_min = ((len(s)-1) * est_var) / chi2_upper
        interval_var_max = ((len(s)-1) * est_var) / chi2_lower

        # 信頼区間に母平均が入った回数
        if interval_mean_min <= mean <= interval_mean_max:
            count_mean += 1

        # 信頼区間に母分散が入った回数
        if interval_var_min <= var <= interval_var_max:
            count_var += 1

    est_means_list.append(est_means)
    est_vars_list.append(est_vars)

    print(f'母平均と標本平均の差の平均：{diff_mean_sum/len(S)}')
    print(f'母分散と標本分散の差の平均：{diff_var_sum/len(S)}')
    print(f'信頼区間に母平均が入る確率：{count_mean/len(S)}')
    print(f'信頼区間に母分散が入る確率：{count_var/len(S)}')
    print()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('default')
sns.set()
sns.set_style('whitegrid')
sns.set_palette('Set1')

x1 = np.random.normal(40, 10, 1000)
x2 = np.random.normal(80, 20, 1000)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.hist([est_means_list[0], est_means_list[1]], bins=30)

plt.show()