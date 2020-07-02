import styles from "./Pantry.module.scss";

import React from "react";
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

export default function Indicator() {
  const dispatch = useDispatch();
  function add(event) {
    event.preventDefault();
    dispatch(explore_add(event.target.elements.choice.value));
  }
  function clear(event) {
    event.preventDefault();
    dispatch(explore_clear());
  }
  function search(event) {
    event.preventDefault();
    dispatch(recipes_update());
  }
  function query(event) {
    dispatch(update_query(event.target.value));
  }
  function bigExplore() {
    dispatch(explore_all());
  }
  let pantry = useSelector((state) => state.pantry);
  let chosen = useSelector((state) => state.explore.ingredients);
  let searchId = "searcher";
  return (
    <div className={styles.pantry}>
      <h1 className="title">The pantry.</h1>
      <form autocomplete="off">
        <div className={`control ${styles.querySearch}`}>
          <input
            id={searchId}
            name="search"
            onChange={query}
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
        <button onClick={bigExplore} className={`${styles.wideButton} button`}>
          Explore with whole pantry
        </button>
      </div>
      <hr />
      <h1 className="title">Raid the pantry.</h1>
      <div className={styles.raidBox}>
        <form onSubmit={add} autocomplete="false">
          <div className="control">
            <label className="label">Choose an ingredient to cook with</label>
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
            <button type="submit" className="button">
              Add
            </button>
            <button onClick={clear} className="button">
              Clear
            </button>
          </div>
        </form>
        <div className="tags">
          {chosen.map((ingredient, idx) => (
            <PantryIngredient
              idx={idx}
              func={explore_remove}
              ingredient={ingredient}
            />
          ))}
        </div>
        <button className="button" onClick={search}>
          Search
        </button>
      </div>
    </div>
  );
}
