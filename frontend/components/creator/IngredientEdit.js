import styles from "./Edit.module.scss";

import { useSelector, useDispatch } from "react-redux";
import Ingredient from "./Ingredient";
import { useState } from "react";
import { add_ingredient } from "../../lib/redux/actions/createAction";
import { update_query } from "../../lib/redux/actions/queryAction";
import Searcher from "./Searcher";

export default function IngredientEdit() {
  const dispatch = useDispatch();
  const searchId = "searcher";
  const initalIngredient = {
    name: "ingredient",
    category: "",
    qty: null,
    adj: "",
    unit: "",
  };
  const [newOne, setNewOne] = useState(initalIngredient);
  const [alert, setAlert] = useState("");
  function fillIngredient(name, category) {
    let updated = { ...newOne };
    updated.name = name;
    updated.category = category;
    setNewOne(updated);
  }
  function clearCat() {
    setNewOne({
      ...newOne,
      category: "",
    });
  }
  function updateIng(event) {
    let updated = { ...newOne };
    updated[event.target.name] = event.target.value;
    setNewOne(updated);
  }
  function addIngredient(event) {
    event.preventDefault();
    if (newOne.category === "") {
      setAlert(
        "Please select a valid ingredient. If it is not in the databse, create it below."
      );
    } else {
      setAlert("");
      let newIngred = {
        adjective: newOne.adj,
        amount: newOne.qty,
        unit: newOne.unit,
        ingredient: {
          name: newOne.name,
          category: {
            name: newOne.category,
          },
        },
      };
      dispatch(add_ingredient(newIngred));
      clearIng();
    }
  }

  function clearIng() {
    let box = document.getElementById("ing-edit-form");
    box.elements.qty.value = null;    
    box.elements.adj.value = "";
    box.elements.unit.value = "";
    document.getElementById(searchId).value = "";
    setNewOne({...initalIngredient});
  }

  let ingredients = useSelector((state) => state.create.ingredients);
  
  return (
    <div>
      <div className="tags">
        {ingredients.map((item, idx) => (
          <Ingredient key={idx} idx={idx} ingredient={item} />
        ))}
      </div>
      <hr />
      <h1 className="title is-4">Add ingredients</h1>
      {alert === "" ? (
        ""
      ) : (
        <div className="tags">
          <div className={`${styles.alert} tag is-danger`}>
            <span>{alert}</span>
            <button onClick={() => setAlert("")} className="delete"></button>
          </div>
        </div>
      )}

      <div className={`field control ${styles.querySearch}`}>
        <input
          onChange={(event) => {
            event.preventDefault();
            clearCat();
            dispatch(update_query(event.target.value));
          }}
          id={searchId}
          className="input"
          placeholder="Search item"
        />
        <Searcher searcher={searchId} func={fillIngredient} />
      </div>

      <form id="ing-edit-form" onSubmit={addIngredient} autoComplete="false">
        <div className="control">
          <div className="field control">
            <input
              required={true}
              onChange={updateIng}
              className="input"
              type="number"
              placeholder="Quantity"
              name="qty"
            />
          </div>
          <div className="field control">
            <input
              required={true}
              onChange={updateIng}
              className="input"
              type="text"
              placeholder="Adjective"
              name="adj"
            />
          </div>
          <div className="field control">
            <input
              required={true}
              onChange={updateIng}
              className="input"
              type="text"
              placeholder="Unit"
              name="unit"
            />
          </div>
          <div className="field control">
            <button style={{ width: "100%" }} className="button is-primary">
              Add Ingredient
            </button>
          </div>
          <div className="field control">
            <button
              onClick={(e) => {e.preventDefault(); clearIng();}}
              style={{ width: "100%" }}
              className="button"
            >
              Clear
            </button>
          </div>
          <div className="field control">
            <label className="label">Preview</label>
            <div className="tags">
              <span className={`tag ${styles.wideTag}`}>
                {`${newOne.qty === null ? "" : newOne.qty} ${
                  newOne.unit === "" ? "" : newOne.unit
                } ${newOne.adj === "" ? "" : newOne.adj} ${newOne.name}`}
              </span>
            </div>
          </div>
        </div>
      </form>
      <hr />
      <h1 className="title is-6">
        Can't find the ingredient you're looking for?{" "}
      </h1>
      <div className="control">
        <button
          style={{ width: "100%" }}
          onClick={() =>
            document
              .getElementById("new-ingredient")
              .classList.toggle("is-active")
          }
          className="button"
        >
          Create Ingredient
        </button>
      </div>
      <br />
    </div>
  );
}
