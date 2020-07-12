import styles from "./Edit.module.scss";

import { useSelector, useDispatch } from "react-redux";
import Ingredient from "./Ingredient";
import { useState } from "react";
import { add_ingredient } from "../../lib/redux/actions/createAction";


export default function IngredientEdit() {
    const dispatch = useDispatch();
    const initalOne = {
        name : "ingredient",
        category : "",
        qty : 0,
        adj : "",
        unit : ""
    }
    const [newOne, setNewOne] = useState(initalOne);
    function updateIng(event) {
        let updated = {...newOne};
        updated[event.target.name] = event.target.value;

        setNewOne(updated);
    }
    function addIngredient(event) {
        event.preventDefault();
        let newIngred = {
            adjective : newOne.adj,
            amount : newOne.qty,
            unit : newOne.unit,
            ingredient : {
                name : newOne.name,
                category : {
                    name : newOne.category
                }
            }
        }
        dispatch(add_ingredient(newIngred));

    }
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
     
        
        <form onSubmit={addIngredient} autocomplete="false">
            <div className="control">
                <div className="field control">
                    <input onChange={updateIng} className="input" type="number" placeholder="Quantity" name="qty"/>
                </div>
                <div className="field control">
                    <input onChange={updateIng} className="input" type="text" placeholder="Adjective" name="adj"/>
                </div>
                <div className="field control">
                    <input onChange={updateIng} className="input" type="text" placeholder="Unit" name="unit"/>
                </div>
                <div className="field control">
                    <button style={{width:"100%"}} className="button is-primary">
                    Add Ingredient
                    </button>
                </div>
                <div className="field control">
                    <button onClick={(e) => {e.preventDefault(); setNewOne(initalOne)}} style={{width:"100%"}} className="button">
                    Clear
                    </button>
                </div>
                <div className="field control">
                    <label className="label">Preview</label>
                    <div className="tags">
                        <span className={`tag ${styles.wideTag}`}>
                            {`${newOne.qty === 0 ? "" : newOne.qty} ${newOne.unit === "" ? "" : newOne.unit} ${newOne.adj === "" ? "" : newOne.adj} ${newOne.name}`}
                        </span>
                    </div>

                </div>
                
            </div>
        </form>
        <hr/>
        <h1 className="title is-6">Can't find the ingredient you're looking for? </h1>
        <div className="control">
            <button style={{width:"100%"}} onClick={() => document.getElementById("new-ingredient").classList.toggle("is-active")} className="button">Create Ingredient</button>
        </div>
        <br/>
    </div>
}