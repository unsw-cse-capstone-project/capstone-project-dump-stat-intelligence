import styles from "./Filter.module.scss";
import Check from "./Check";
import FilterItem from "./FilterItem";
import { recipes_update } from "../../lib/redux/actions/recipesAction";

import { useSelector, useDispatch } from "react-redux";

export default function Filter() {
  const dispatch = useDispatch();
  let filters = useSelector(state => state.explore.filters)
  return (
    <div className="field is-grouped">
      <div className="control">
        <div class="select dropdown is-hoverable">
          <div class="dropdown-trigger">
            <button class="button" aria-haspopup="true" aria-controls="dropdown-menu4">
              <span>Meal type</span>
              <span class="icon is-small">
                <i class="fas fa-check" aria-hidden="true"></i>
              </span>
            </button>
          </div>
          <div class="dropdown-menu" id="dropdown-menu4" role="menu">
            <div className="dropdown-content">
              {Object.keys(filters.meal).map((key, idx) => (
                <FilterItem idx={idx} category="meal" name={key} is_checked={filters.meal[key]}/>
              ))}
            </div>
          </div>
        </div>
      </div>
      <div className="control">
        <div class="select dropdown is-hoverable">
          <div class="dropdown-trigger">
            <button class="button" aria-haspopup="true" aria-controls="dropdown-menu4">
              <span>Dietary requirements</span>
              <span class="icon is-small">
                <i class="fas fa-check" aria-hidden="true"></i>
              </span>
            </button>
          </div>
          <div class="dropdown-menu" id="dropdown-menu4" role="menu">
            <div className="dropdown-content">
              {Object.keys(filters.diet).map((key, idx) => (
                <FilterItem idx={idx} category="diet" name={key} is_checked={filters.diet[key]}/>
              ))}
            </div>
          </div>
        </div>
      </div>
      <div className="control">
        <button onClick={(event) => {event.preventDefault(); dispatch(recipes_update());}} className="button"><span>Filter</span></button>
      </div>
    </div>
  );
}
