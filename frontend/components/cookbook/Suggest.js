import styles from "./Cookbook.module.scss";

import { useState, useEffect } from 'react';
import Link from "next/link";
import recipeAPI from "../../lib/api/recipe"
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
        <div className={styles.sug}>
            <h3 className="title is-5">Feeling creative? Make a recipe with these commonly searched ingredients.</h3>
        </div>
        <div className={`${styles.choice} tags`}>
            {
                ingredients.map((val, idx) => (
                    <span key={idx} className="tag is-dark">
                        {val}
                    </span>
                ))
            }
        </div>
        <div className={styles.dewit}>
            <Link href={"/recipe/create"}>
                <a className="is-link">Start creating</a>
            </Link>
        </div>
    </div>
}