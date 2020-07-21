import styles from "./Cookbook.module.scss";

import { useState, useEffect } from 'react';
import Link from "next/link";
import recipeAPI from "../../lib/api/recipe"
import RecipeAPI from "../../lib/api/recipe";




export default function Suggest() {

    const [ingredients, setIngredients] = useState([]);


    useEffect(() => {
        RecipeAPI.discover()
        .then(res => console.log(res))
        .catch(err => console.log(err))
    }, [])

    return <div className={styles.suggestion}>
        <div className={styles.sug}>
            <h3 className="title is-5">Feeling creative? Make a recipe with these commonly searched ingredients.</h3>
        </div>
        <div className={styles.choice}>
            corinader
        </div>
        <div className={styles.dewit}>
            <Link href={"/recipe/create"}>
                <a className="is-link">Start creating</a>
            </Link>
        </div>
    </div>
}