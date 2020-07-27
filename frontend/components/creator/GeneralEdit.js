import styles from "./Edit.module.scss";

import { useSelector, useDispatch } from 'react-redux';
import { update_create, add_category, remove_category } from "../../lib/redux/actions/createAction";
import DropItem from "./DropItem";

export default function GeneralEdit() {
    const dispatch = useDispatch();
    let recipe = useSelector(state => state.create)
    function handleInput(event) {
        dispatch(update_create(event.target.name, event.target.value));
    }
    //Need to do some processing because data in backend is different
    let meal = {
        Breakfast : false,
        Lunch : false,
        Dinner : false,
        Snack : false,
        Dessert : false,
        Brunch : false
    }
    let diet = {
        Vegan : false,
        Vegetarian : false,
        "Gluten-free" : false,
        "Dairy-free" : false
    }
    recipe.meal_cat.map(cat => {
        meal[cat.name] = true;
    })
    recipe.diet_req.map(dietar => {
        diet[dietar.name] = true
    })

    return <div className="form">
        <div className="field control">
            <label className="label">Title</label>
            <input
                name="name"
                className="input"
                type="text"
                value={recipe.name}
                onChange={handleInput}
            />
        </div>
        <div className="field control">
            <label className="label">Cook time</label>
            <input
                name="cook_time"
                className="input"
                type="text"
                value={recipe.cook_time}
                onChange={handleInput}
            />
        </div>
        <div className="field control">
            <label className="label">Image URL</label>
            <input
                name="image_URL"
                className="input"
                type="text"
                value={recipe.image_URL}
                onChange={handleInput}
            />
        </div>
        <div className="field control">
        <label className="label">Meal type</label>
            <div className="select dropdown is-hoverable" style={{width:"100%"}}>
                <div style={{width:"100%"}} className="dropdown-trigger">
                <button
                    className="button"
                    style={{width:"100%"}}
                    aria-haspopup="true"
                    aria-controls="dropdown-menu4"
                >
                    <span>Meal type</span>
                    <span className="icon is-small">
                    <i className="fas fa-check" aria-hidden="true"></i>
                    </span>
                </button>
                </div>
                <div style={{width:"100%"}} className="dropdown-menu" id="dropdown-menu4" role="menu">
                <div className="dropdown-content">
                    {Object.keys(meal).map((key, idx) => (
                    <DropItem
                        key={idx}
                        name={key}
                        is_checked={meal[key]}
                        add={add_category}
                        remove={remove_category}
                        category="meal_cat"
                    />
                    ))}
                </div>
                </div>
          </div>
        </div>
        <div className="field control">
            <label className="label">Dietary requirements</label>
            <div className="select dropdown is-hoverable" style={{width:"100%"}}>
                <div style={{width:"100%"}} className="dropdown-trigger">
                <button
                    className="button"
                    style={{width:"100%"}}
                    aria-haspopup="true"
                    aria-controls="dropdown-menu4"
                >
                    <span>Dietary requirements</span>
                    <span className="icon is-small">
                    <i className="fas fa-check" aria-hidden="true"></i>
                    </span>
                </button>
                </div>
                <div style={{width:"100%"}} className="dropdown-menu" id="dropdown-menu4" role="menu">
                <div className="dropdown-content">
                    {Object.keys(diet).map((key, idx) => (
                    <DropItem
                        key={idx}
                        name={key}
                        is_checked={diet[key]}
                        add={add_category}
                        remove={remove_category}
                        category="diet_req"
                    />
                    ))}
                </div>
            </div>
          </div>
        </div>
    </div>


}