
多行连等:
\begin{aligned} 
P(x_5) 
&= \sum_{x_4} \sum_{x_3} \sum_{x_2} \sum_{x_1} P(x_1, x_2, x_3, x_4, x_5) \\
&= \sum_{x_4} \sum_{x_3} \sum_{x_2} \sum_{x_1} P(x_1) P(x_2 | x_1) P(x_3 | x_2) P(x_4 | x_3) P(x_5 | x_3)
\end{aligned}

&用于对齐,`\\`用来换行

可以带上大括号,用\begin{cases} ,\end{cases}
\begin{cases} 
V_T(x) = \max_{a \in A} \sum_{x' \in X} P^a_{x \to x'} \left( \frac{1}{T} R^a_{x \to x'} + \frac{T-1}{T} V_{T-1}(x') \right); \\ 
V_\gamma(x) = \max_{a \in A} \sum_{x' \in X} P^a_{x \to x'} \left( R^a_{x \to x'} + \gamma V_\gamma(x') \right). 
\end{cases}
\tag{16.18}


加上公式结尾加上序号 \tag{1}

映射: \mapsto 
$\mathbb R$:\mathbb R

$\mathbf x$: \mathbf x
$\boldsymbol x$ :\boldsymbol x
$\mathcal X$: \mathcal X      $\mathcal L$:\mathcal L

加减乘除 \times $\times$       \div $\div$

逻辑
$\land$  $\lnot$  $\lor$    \land   lnot  lor


`\; \; `可以实现空格 $x \, y \; z$ 