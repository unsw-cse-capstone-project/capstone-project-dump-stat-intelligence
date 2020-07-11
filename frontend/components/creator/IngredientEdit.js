import styles from "./Edit.module.scss";

import { useSelector, useDispatch } from "react-redux";
import Ingredient from "./Ingredient";
import NewIngredient from "./NewIngredient";

export default function IngredientEdit() {
    let ingredients = useSelector(state => state.create.ingredients);
    let searchId="searcher"
    return <div>
        <div className="tags">
            {ingredients.map((item, idx) => (
                <Ingredient key={idx} idx={idx} ingredient={item}/>
            ))}
        </div>
        
        <h1 className="title is-4">Add ingredients</h1>
        <div className={`control ${styles.querySearch}`}>
            <input id={searchId} className="input" placeholder="Add an item"/>
        </div>
        <form onSubmit={(event) => {event.preventDefault(); dispatch(explore_add(event.target.elements.choice.value));}} autocomplete="false">
            <div className="control">
                <label className="label">Choose an ingredient to cook with</label>
                <div className={`field is-grouped ${styles.formCon}`}>
                    <div className="control">
                        <input className="input"/>
                    </div>
                    
                    <div className="control">
                        <button type="submit" className="button">
                            Add
                        </button>
                    </div>
                    <div className="control">
                        <button onClick={(event) => basic_dispatch(event, explore_clear)} className="button">
                        Clear
                        </button>
                    </div>
                </div>
            </div>
        </form>
        <h1 className="title is-6">Can't find the ingredient you're looking for? </h1>
        <div className="control">
            <button style={{width:"100%"}} onClick={() => document.getElementById("new-ingredient").classList.toggle("is-active")} className="button">Create Ingredient</button>
        </div>
        
    </div>
}