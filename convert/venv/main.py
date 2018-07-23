def main(fname):
    with open(fname,'r') as f,open('restUN.txt','w') as og,open('positive.parsed','w') as p,open('negative.parsed','w') as n:
        og.write('<reviews>')
        n.write('<reviews>')
        p.write('<reviews>')
        num_reviews = 0
        num_p = 0
        num_n = 0
        for line in f:
            num_reviews += 1
            if num_reviews >= 7000:
                break
            grade = int(line[0])
            if grade == 3:
                continue
            review = "<review>{}</review>\n".format(line[2:].replace('&',' and '))
            og.write(review)
            if grade > 3:
                if num_p < 1000:
                    num_p += 1
                    p.write(review)
            else:
                if num_n < 1000:
                    num_n += 1
                    n.write(review)
        og.write('</reviews>')
        p.write('</reviews>')
        n.write('</reviews>')

if __name__ == '__main__':
    main('1-restaurant-train.csv')