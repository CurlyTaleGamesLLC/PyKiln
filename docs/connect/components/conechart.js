Vue.component('conechart', {
    template: `
    <table class="table table-striped text-center">  
        <thead>
        <tr class="cone-row">
            <th class="d-none"></th>
            <th>Cone #</th>
            <th>27°F/HOUR</th>
            <th>108°F/HOUR</th>
            <th>270°F/HOUR</th>
        </tr>
        </thead>
        <tbody id="cone-table">
        <tr class="cone-row"></td>
            <td>022</td>
            <td>1049°F</td>
            <td>1087°F</td>
            <td>1094°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>021</td>
            <td>1076°F</td>
            <td>1112°F</td>
            <td>1143°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>020</td>
            <td>1125°F</td>
            <td>1159°F</td>
            <td>1180°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>019</td>
            <td>1213°F</td>
            <td>1252°F</td>
            <td>1283°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>018</td>
            <td>1267°F</td>
            <td>1319°F</td>
            <td>1353°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>017</td>
            <td>1301°F</td>
            <td>1360°F</td>
            <td>1405°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>016</td>
            <td>1368°F</td>
            <td>1422°F</td>
            <td>1465°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>015</td>
            <td>1382°F</td>
            <td>1456°F</td>
            <td>1504°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>014</td>
            <td>1395°F</td>
            <td>1485°F</td>
            <td>1540°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>013</td>
            <td>1485°F</td>
            <td>1539°F</td>
            <td>1582°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>012</td>
            <td>1549°F</td>
            <td>1582°F</td>
            <td>1620°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>011</td>
            <td>1575°F</td>
            <td>1607°F</td>
            <td>1641°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>010</td>
            <td>1636°F</td>
            <td>1657°F</td>
            <td>1679°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>09</td>
            <td>1665°F</td>
            <td>1688°F</td>
            <td>1706°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>08</td>
            <td>1692°F</td>
            <td>1728°F</td>
            <td>1753°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>07</td>
            <td>1764°F</td>
            <td>1789°F</td>
            <td>1809°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>06</td>
            <td>1798°F</td>
            <td>1828°F</td>
            <td>1855°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>05½</td>
            <td>1839°F</td>
            <td>1859°F</td>
            <td>1877°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>05</td>
            <td>1870°F</td>
            <td>1888°F</td>
            <td>1911°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>04</td>
            <td>1915°F</td>
            <td>1945°F</td>
            <td>1971°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>03</td>
            <td>1960°F</td>
            <td>1987°F</td>
            <td>2019°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>02</td>
            <td>1972°F</td>
            <td>2016°F</td>
            <td>2052°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>01</td>
            <td>1999°F</td>
            <td>2046°F</td>
            <td>2080°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>1</td>
            <td>2028°F</td>
            <td>2079°F</td>
            <td>2109°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>2</td>
            <td>2034°F</td>
            <td>2088°F</td>
            <td>2127°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>3</td>
            <td>2039°F</td>
            <td>2106°F</td>
            <td>2138°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>4</td>
            <td>2086°F</td>
            <td>2124°F</td>
            <td>2161°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>5</td>
            <td>2118°F</td>
            <td>2167°F</td>
            <td>2205°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>5½</td>
            <td>2133°F</td>
            <td>2197°F</td>
            <td>2237°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>6</td>
            <td>2165°F</td>
            <td>2232°F</td>
            <td>2269°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>7</td>
            <td>2194°F</td>
            <td>2262°F</td>
            <td>2295°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>8</td>
            <td>2212°F</td>
            <td>2280°F</td>
            <td>2320°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>9</td>
            <td>2235°F</td>
            <td>2300°F</td>
            <td>2336°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>10</td>
            <td>2284°F</td>
            <td>2345°F</td>
            <td>2381°F</td>
        </tr>
        <tr class="cone-row"></td>
            <td>11</td>
            <td>2322°F</td>
            <td>2361°F</td>
            <td>2399°F</td>
        </tr>
    </tbody>
</table>
    `
});