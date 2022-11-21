import React, { useState, useEffect } from 'react';

import { Chart } from "react-google-charts";
import TransactionsApi from '../data/transactionsApi';


export const headers = ["category_name", "Total Amount ₪"];

export const options = {
    pieSliceText: "value",
    title: "My Transactions",
};

function Breakdowns(props) {
    const [breakdowns, setBreakdowns] = useState([])

    const getBreakDowns = () => {
        TransactionsApi.getBreakdowns()
            .then((data) => [headers, ...data.map(breakDown => [breakDown['category_name'], breakDown['amount_sum']])])
            .then(breakdowns => setBreakdowns(breakdowns))
            .catch((err) => {
                console.error(err)
            })
    }

    console.log(breakdowns)

    useEffect(() => { getBreakDowns() }, [])

    return (
        <Chart
            chartType="BarChart"
            data={breakdowns}
            options={options}
            width={"100%"}
            height={"400px"}
            pieSliceText="text"
        />
    );
}
export default Breakdowns;