import random
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns


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
        diff_mean_sum += (mean - est_mean)**2
        diff_var_sum += (var - est_var)**2

        # 平均の95%信頼区間の計算
        # 統計量tを求める
        t_mean = (est_mean - mean)/np.sqrt(est_var/len(s))
        # t分布の上側2.5%点を求める（自由度はsample_num-1）
        t_upper = stats.t.ppf(0.975, len(s)-1)
        # 信頼区間の計算
        interval_mean_min = est_mean - t_upper * np.sqrt(est_var/len(s))
        interval_mean_max = est_mean + t_upper * np.sqrt(est_var/len(s))

        # カイ二乗分布の上側2.5%点と下側2.5%点を求める（自由度はsample_num-1）
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

    print(f'母平均と標本平均の差の分散：{diff_mean_sum/(len(S)-1)}')
    print(f'母分散と標本分散の差の分散：{diff_var_sum/(len(S)-1)}')
    print(f't分布の上側2.5%点{t_upper}')
    print(f'カイ二乗分布の上側2.5%点{chi2_upper}')
    print(f'カイ二乗分布の下側2.5%点{chi2_lower}')
    print(f'信頼区間に母平均が入る確率：{count_mean/len(S)}')
    print(f'信頼区間に母分散が入る確率：{count_var/len(S)}')
    print()

plt.style.use('default')
sns.set()
sns.set_style('whitegrid')
sns.set_palette('Set1')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.hist([est_means_list[0], est_means_list[1]], bins=30, label=["sample number is 10","sample number is 100"])
ax.set_xlabel('class value')
ax.set_ylabel('frequency')
plt.legend()
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.hist([est_vars_list[0], est_vars_list[1]], bins=30, label=["sample number is 10","sample number is 100"])
ax.set_xlabel('class value')
ax.set_ylabel('frequency')
plt.legend()
plt.show()