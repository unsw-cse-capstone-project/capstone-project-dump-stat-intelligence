import styles from "./Pantry.module.scss";

import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import PantryIngredient from "./PantryIngredient";
import { remove, get_pantry } from "../../lib/redux/actions/pantryAction";
import {
  explore_remove,
  explore_add,
  explore_clear,
} from "../../lib/redux/actions/exploreAction";
import { recipes_update } from "../../lib/redux/actions/recipesAction";
import { update_query } from "../../lib/redux/actions/queryAction";
import IngredientSearch from "./IngredientSearch";
import { explore_all } from "../../lib/redux/actions/exploreAction";
import { useRouter } from 'next/router';

import Arrow from "./Arrow";



export default function Pantry() {
  const router = useRouter();
    
  const dispatch = useDispatch();
  function basic_dispatch(event, func) {
    event.preventDefault();
    dispatch(func());
  }
  let pantry = useSelector((state) => state.pantry);
  let chosen = useSelector((state) => state.explore.ingredients);
  let searchId = "searcher";

  let isExplore = router.pathname === '/explore'


  return (
    <div id="pantry" className={styles.pantry}>
      
      
      <div id="pantry-head" className={`${styles.header}`}><div className={styles.title}>The pantry.</div></div>
      
      <IngredientSearch id={"pantry-query"} searcher={searchId} />
      <div id="pantry-box" className={styles.drawer}>
        <br/>
        <form autoComplete="off">
          <div onFocus={() => document.getElementById("pantry-query").classList.toggle(styles.show)} onBlur={() => setTimeout(() => document.getElementById("pantry-query").classList.remove(styles.show), 200)} className={`control ${styles.querySearch}`}>
            <input
              id={searchId}
              name="search"
              onChange={(event) => {event.preventDefault(); dispatch(update_query(event.target.value));}}
              className="input"
              placeholder="Add an item"
            />
          </div>
        </form>
        <div className={styles.ingredientSection}>
          {Object.keys(pantry).map((category, i) => {
            if (pantry[category].length !== 0 && category !== 'meta') {
              return (
                <div key={i}>
                  <h4>{category}</h4>
                  <div className="tags">
                    {pantry[category].map((ingredient, j) => (
                      <PantryIngredient
                        func={remove}
                        idx={j}
                        key={j}
                        ingredient={ingredient.name}
                        category={category}
                        expiry={ingredient.expiry}
                      />
                    ))}
                  </div>
                </div>
              );
            }
          })}
          { isExplore ? <>
            <br />
            <button onClick={(event) => {basic_dispatch(event, explore_all)}} className={`${styles.wideButton} button`}>
              Explore with whole pantry
            </button>
          </> : "" }
        </div>
      </div>
      
    </div>
  );
}
