import styles from "./Pantry.module.scss";

import React from "react";
import { useSelector, useDispatch } from 'react-redux';
import PantryIngredient from './PantryIngredient';
import { remove } from "../../lib/redux/actions/pantryAction";
import { explore_remove, explore_add, explore_clear } from "../../lib/redux/actions/exploreAction";

export default function Indicator() {
  const dispatch = useDispatch();
  function add(event) {
    console.log("YEET");
    event.preventDefault();
    dispatch(explore_add(event.target.elements.choice.value));
  }
  function clear(event) {
    
    event.preventDefault();
    dispatch(explore_clear());
  }
  let pantry = useSelector(state => state.pantry)
  let chosen = useSelector(state => state.explore)
  return (
    <div className={styles.pantry}>
      <h1 className="title">The pantry.</h1>
      <div className="control">
        <input className="input" placeholder="Add an item" />
      </div>
      <div className={styles.ingredientSection}>
        {Object.keys(pantry).map((category, i) => {
          if (pantry[category].length !== 0) {
            return <div key={i}>
              <h4>{category}</h4>
              <div className="tags">
                {pantry[category].map((ingredient, j) => (
                  <PantryIngredient func={remove} idx={j} ingredient={ingredient.name} category={category}/>
                ))}
              </div>
            </div>
          }


        })}
      </div>
      <form onSubmit={add}>
        <h3 className="subtitle is-3">Raid the pantry</h3>
        <div className="control">
          <label className="label">Choose an ingredient to cook with</label>
          <div className="select">
            <select name="choice">
              {Object.keys(pantry).map((category, i) => {
                return <>
                  {pantry[category].map((ingredient,j) => (
                    ( chosen.indexOf(ingredient.name) === -1 ?
                      <option key={j}>{ingredient.name}</option>
                      : ""
                    )
                    
                  ))}
                </> 
              })}
            </select>
          </div>
          <button type="submit" className="button">Add</button>
          <button onClick={clear} className="button">Clear</button>
        </div>
      </form>
      <div className={styles.ingredientSection}>
        {chosen.map((ingredient, idx) => (
          <PantryIngredient idx={idx} func={explore_remove} ingredient={ingredient} />
        ))}
      </div>
    </div>
  );
}

