 #                          智慧海洋
第一次比赛进入复赛，最后由于准备期末搁浅，虽然说最后没有一个特别优异的成绩，但是确实是一次很棒的体验和提升  
选择海洋赛也是因为数据简单，全靠自己挖掘，相对来说新手上手容易，相信我，一点一点看代码，一定会有所收获。  

代码直接上了jupyter里做的，代码里大部分都注释讲解了

思路：  
1.判断渔船是否处于静止状态：是否存在连续较多个0值  
2.离群点： 第一类是由于海面颠簸造成的突然速度变化，这类点难以检测，只去除了在静止状态时由于颠簸所造成的突然速度变化。 其他离群点：去除速度过快的点
  尝试利用高斯－克吕格平面直角坐标系还原还原经纬度坐标，剔除海域外的坐标点
3.构建特征
1）万物皆可统计，先构造简单的统计学特征 均值 众数 中位数 方差 标准差 极值等
2）对速度角度进行分段统计，难点：该以什么标准分段。 先进行可视化展示，然后多次尝试不同分段结果，得到一组准确率较高的分段统计结果
3）时间序列无法作为特征，但经过处理的数据可以统计主要工作时段，亦可作为重要特征

4）工作海域 ，速度变化快慢，角度变化快慢，坡度等特征






