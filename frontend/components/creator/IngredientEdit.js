import styles from "./Edit.module.scss";

import { useSelector, useDispatch } from "react-redux";
import Ingredient from "./Ingredient";
import NewIngredient from "./NewIngredient";
import { useState } from "react";


export default function IngredientEdit() {
    const [newOne, setNewOne] = useState({});
    
    let ingredients = useSelector(state => state.create.ingredients);
    let searchId="searcher"
    return <div>
        <div className="tags">
            {ingredients.map((item, idx) => (
                <Ingredient key={idx} idx={idx} ingredient={item}/>
            ))}
        </div>
        <hr/>
        <h1 className="title is-4">Add ingredients</h1>
        <div className={`field control ${styles.querySearch}`}>
            <input id={searchId} className="input" placeholder="Search item"/>
        </div>
     
        
        <form autocomplete="false">
            <div className="control">
                <div className="field control">
                    <input className="input" type="number" placeholder="Quantity" name="qty"/>
                </div>
                <div className="field control">
                    <input className="input" type="text" placeholder="Adjective" name="adj"/>
                </div>
                <div className="field control">
                    <input className="input" type="text" placeholder="Unit" name="unit"/>
                </div>
                <div className="field control">
                    <button style={{width:"100%"}} className="button">
                    Clear
                    </button>
                </div>
                <div className="field control">
                    <label className="label">Preview</label>
                    <div className="tags">
                        <span className={`tag ${styles.wideTag}`}>BRUH</span>
                    </div>

                </div>
                <div className="field control">
                    <button style={{width:"100%"}} className="button is-primary">
                    Add Ingredient
                    </button>
                </div>
            </div>
        </form>
        <hr/>
        <h1 className="title is-6">Can't find the ingredient you're looking for? </h1>
        <div className="control">
            <button style={{width:"100%"}} onClick={() => document.getElementById("new-ingredient").classList.toggle("is-active")} className="button">Create Ingredient</button>
        </div>
        
    </div>
}