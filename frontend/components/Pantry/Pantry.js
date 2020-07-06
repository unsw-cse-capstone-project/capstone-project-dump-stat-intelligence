import styles from "./Pantry.module.scss";

import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import PantryIngredient from "./PantryIngredient";
import { remove } from "../../lib/redux/actions/pantryAction";
import {
  explore_remove,
  explore_add,
  explore_clear,
} from "../../lib/redux/actions/exploreAction";
import { recipes_update } from "../../lib/redux/actions/recipesAction";
import { update_query } from "../../lib/redux/actions/queryAction";
import IngredientSearch from "./IngredientSearch";
import { explore_all } from "../../lib/redux/actions/exploreAction";

import Arrow from "./Arrow";



export default function Indicator() {
  function toggleIt(id) {
    document.getElementById(id + "-icon").classList.toggle(styles.arrowUp);
    let box = document.getElementById(id + "-box")
    if (box.style.maxHeight) {
      box.style.maxHeight = box.scrollHeight + 'px';
      setTimeout(() => {box.style.maxHeight = null},5);
    } else {
      box.style.maxHeight = box.scrollHeight + 'px';
      setTimeout(() => {box.style.maxHeight = 'none'},305)
    }
  }
  
  const dispatch = useDispatch();
  function basic_dispatch(event, func) {
    event.preventDefault();
    dispatch(func());
  }
  let pantry = useSelector((state) => state.pantry);
  let chosen = useSelector((state) => state.explore.ingredients);
  let searchId = "searcher";
  return (
    <div id="pantry" className={styles.pantry}>
      
      
      <div id="pantry-head" onClick={() => toggleIt("pantry")} className={`${styles.header}`}><div className={styles.title}>The pantry.</div><Arrow name="pantry-icon" /></div>
      
      <div id="pantry-box" className={styles.drawer}>
        <br/>
        <form autoComplete="off">
          <div className={`control ${styles.querySearch}`}>
            <input
              id={searchId}
              name="search"
              onChange={(event) => {event.preventDefault(); dispatch(update_query(event.target.value));}}
              className="input"
              placeholder="Add an item"
            />
            <IngredientSearch searcher={searchId} />
          </div>
        </form>
        <div className={styles.ingredientSection}>
          {Object.keys(pantry).map((category, i) => {
            if (pantry[category].length !== 0) {
              return (
                <div key={i}>
                  <h4>{category}</h4>
                  <div className="tags">
                    {pantry[category].map((ingredient, j) => (
                      <PantryIngredient
                        func={remove}
                        idx={j}
                        ingredient={ingredient.name}
                        category={category}
                      />
                    ))}
                  </div>
                </div>
              );
            }
          })}
          <br />
          <button onClick={(event) => basic_dispatch(event, explore_all)} className={`${styles.wideButton} button`}>
            Explore with whole pantry
          </button>
        </div>
      </div>
      
      <hr />
          
      <div id="search-head" onClick={() => toggleIt("search")} className={`${styles.header}`}><div className={styles.title}>Raid the pantry</div><Arrow name="search-icon"/></div>

      <div id="search-box" className={styles.drawer}>

        {Object.keys(pantry).length === 0 && chosen.length === 0 
        ? 
          <div className="control">
            <br/>
            <label className="label">Add some ingredients to your pantry above to start searching for recipes!</label>
          </div>  
        : 
          <div className={styles.raidBox}>
            <br/>
            <form onSubmit={(event) => {event.preventDefault(); dispatch(explore_add(event.target.elements.choice.value));}} autocomplete="false">
              <div className="control">
                <label className="label">Choose an ingredient to cook with</label>
                <div className={`field is-grouped ${styles.formCon}`}>
                  <div className="control">
                    <div className="select">
                      <select name="choice">
                        {Object.keys(pantry).map((category, i) => {
                          return (
                            <>
                              {pantry[category].map((ingredient, j) =>
                                chosen.indexOf(ingredient.name) === -1 ? (
                                  <option key={j}>{ingredient.name}</option>
                                ) : (
                                  ""
                                )
                              )}
                            </>
                          );
                        })}
                      </select>
                    </div>
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
            <div className={styles.searchSection}>
              <div className="tags">
                {chosen.map((ingredient, idx) => (
                  <PantryIngredient
                    idx={idx}
                    func={explore_remove}
                    ingredient={ingredient}
                  />
                ))}
              </div>
            </div>
            <button className={`button ${styles.wideButton}`} onClick={(event) => basic_dispatch(event, recipes_update)}>
              Search
            </button>
          </div>
        }
      </div>
    </div>
  );
}
