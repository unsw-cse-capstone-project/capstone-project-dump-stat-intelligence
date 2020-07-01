import styles from "./Pantry.module.scss";

import React from "react";
import { useSelector } from 'react-redux';
import PantryIngredient from './PantryIngredient';

export default function Indicator() {

  let pantry = useSelector(state => state.pantry)
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
                  <PantryIngredient key={j} ingredient={ingredient.name} category={category}/>
                ))}
              </div>
            </div>
          }


        })}
      </div>
    </div>
  );
}

