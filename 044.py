
if __name__ == "__main__":
    pentagons = list(int(i*(3*i-1)/2) for i in range(1, 10000))
    ans = min(abs(k-j) for k in pentagons for j in pentagons if k +
              j in pentagons and abs(k-j) in pentagons)
    print(ans)
