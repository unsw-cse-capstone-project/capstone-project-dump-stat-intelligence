import styles from "./Edit.module.scss";

import { useState, useEffect } from 'react';
import Link from "next/link";
import RecipeAPI from "../../lib/api/recipe";




export default function Suggest() {

    const [ingredients, setIngredients] = useState([
        "coriander", "chicken"
    ]);


    useEffect(() => {
        RecipeAPI.discover()
        .then(res => {
            let ings = res.data.search.split(",");
            for (let i = 0; i < ings.length; i++) {
                ings[i] = ings[i].split("|").join(" ")
            }
            setIngredients(ings)

        })
        .catch(err => console.log(err))
    }, [])

    return <div className={styles.suggestion}>
        
        
        <div className={`${styles.choice} tags`}>
            <span className="is-6">Need inspiration? Use these commonly searched ingredients - </span>
            {
                ingredients.map((val, idx) => (
                    <span key={idx} className="tag is-dark">
                        {val}
                    </span>
                ))
            }
        </div>
    </div>
}