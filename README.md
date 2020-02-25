# graphillion_tutorial

グラフ集合処理ライブラリ(Graphillion)[https://github.com/takemaru/graphillion/wiki] のチュートリアルです．本チュートリアルを通じて，Graphillionを用いたグラフ集合処理の基本を学ぶことができます．

チュートリアル中のコードはすべて(Google Colaboratory)[https://colab.research.google.com/]上で動かすことができます．Google Colaboratoryを利用するためにはGoogleアカウントが必要です．

## 目次
以下のリンクから各コンテンツをGoogle Colaboratoryで開くことができます．

1. [はじめに](https://colab.research.google.com/github/nsnmsak/graphillion_tutorial/blob/master/ja/01_introduction.ipynb)
2. [グラフ入門](https://colab.research.google.com/github/nsnmsak/graphillion_tutorial/blob/master/ja/02_graph_theory.ipynb):  本チュートリアルを理解するために必要となるグラフ理論の基礎について説明します．グラフとは何か，なぜグラフ理論が有益なのかを簡単に説明します．既にグラフ理論に習熟されている方は次章に進んでください．

3. [グラフと組合せ爆発](https://colab.research.google.com/github/nsnmsak/graphillion_tutorial/blob/master/ja/03_graph_and_combinatorial_explosion.ipynb): グラフの問題を解く際，しばしば指数的に存在する部分グラフを扱わなければならない場面がでてきます．この章ではそのような組合せ爆発について解説します．

4. [Graphillionに触れてみよう](https://colab.research.google.com/github/nsnmsak/graphillion_tutorial/blob/master/ja/04_graphillion_first_step.ipynb): いよいよGraphillionの説明に入ります．ま←あ有名な「数え上げお姉さん問題」を題材に，Graphillionを用いたグラフ集合処理の例を紹介します．

5. [Graphillionの内部](https://colab.research.google.com/github/nsnmsak/graphillion_tutorial/blob/master/ja/05_graphillion_and_zdd.ipynb): Graphillionの内部ではZDDとよばれるデータ構造が利用されています．GraphillionはZDDを意識せずとも利用することができますが，Graphillionの挙動を理解するためにはZDDの理解が不可欠です．この章ではGraphillionにおいてZDDが果たす役割について説明します．

6. [GraphSet](https://colab.research.google.com/github/nsnmsak/graphillion_tutorial/blob/master/ja/06_graph_set.ipynb): Graphillionではグラフの集合を表すGraphSetとよばれるオブジェクトを作成し，様々な操作を実行することができます．この章ではGraphSetに対して行える代表的な操作を紹介します．

7. [Graphillionによる最適化](https://colab.research.google.com/github/nsnmsak/graphillion_tutorial/blob/master/ja/07_answering_path_query.ipynb): Graphillionを用いることで，グラフに関する最適化問題を解くことができます．この章ではGraphillionを用いて最適化問題を解く方法と，Graphillionが得意とする最適化問題の種類について説明します．
8. [ネットワーク信頼性の計算](https://colab.research.google.com/github/nsnmsak/graphillion_tutorial/blob/master/ja/08_network_reliability.ipynb): Graphillionの機能を活用することで，ネットワークの故障に対する強さを調べることができます．
9. [Graphillion 実践ガイド](https://colab.research.google.com/github/nsnmsak/graphillion_tutorial/blob/master/ja/09_practtical_guide.ipynb) Graphillionで効率的に問題を解くための指針をいくつか紹介します．