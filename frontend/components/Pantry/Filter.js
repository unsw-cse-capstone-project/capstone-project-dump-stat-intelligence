import styles from "./Filter.module.scss";
import FilterItem from "./FilterItem";
import { recipes_update } from "../../lib/redux/actions/recipesAction";
import { useSelector, useDispatch } from "react-redux";
import { update_search } from "../../lib/redux/actions/searchAction";
import FilterSearch from "./FilterSearch";

export default function Filter() {
  const dispatch = useDispatch();
  let filters = useSelector((state) => state.explore.filters);
  let selections = useSelector(state => state.explore.ingredients)
  return (
    <div className={`form ${styles.filter}`} autoComplete="off">
      <div className="field is-grouped">
        <div className={`control ${styles.searchFormBox}`} onFocus={() => document.getElementById("explore-ing-add").classList.toggle(styles.show)} onBlur={() => setTimeout(() => document.getElementById("explore-ing-add").classList.remove(styles.show), 200)}>
          <FilterSearch id={"explore-ing-add"} searcher="explore-search"/>
          <input id="explore-search" placeholder="Add an ingredient" className="input" name="search" onChange={(e => {e.preventDefault(); dispatch(update_search(e.target.value))})}/>
          
        </div>
        <div className="control">
          <button onClick={e => {e.preventDefault();}} className="button">clear</button>
        </div>
      </div>
      
      
      <div className="field is-grouped">
        <div className="control">
          <div className="select dropdown is-hoverable">
            <div className="dropdown-trigger">
              <button
                className="button"
                aria-haspopup="true"
                aria-controls="dropdown-menu4"
              >
                <span>Meal type</span>
                <span className="icon is-small">
                  <i className="fas fa-check" aria-hidden="true"></i>
                </span>
              </button>
            </div>
            <div className="dropdown-menu" id="dropdown-menu4" role="menu">
              <div className="dropdown-content">
                {Object.keys(filters.meal).map((key, idx) => (
                  <FilterItem
                    key={idx}
                    idx={idx}
                    category="meal"
                    name={key}
                    is_checked={filters.meal[key]}
                  />
                ))}
              </div>
            </div>
          </div>
        </div>
        <div className="control">
          <div className="select dropdown is-hoverable">
            <div className="dropdown-trigger">
              <button
                className="button"
                aria-haspopup="true"
                aria-controls="dropdown-menu4"
              >
                <span>Dietary requirements</span>
                <span className="icon is-small">
                  <i className="fas fa-check" aria-hidden="true"></i>
                </span>
              </button>
            </div>
            <div className="dropdown-menu" id="dropdown-menu4" role="menu">
              <div className="dropdown-content">
                {Object.keys(filters.diet).map((key, idx) => (
                  <FilterItem
                    key={idx}
                    category="diet"
                    name={key}
                    is_checked={filters.diet[key]}
                  />
                ))}
              </div>
            </div>
          </div>
        </div>
        <div className="control">
          <button
            onClick={(event) => {
              event.preventDefault();
              dispatch(recipes_update());
            }}
            className="button is-primary"
          >
            <span>Search</span>
          </button>
        </div>
      </div>
      {/** 
      <div className="field tags">
          {Object.keys(filters.meal).map((key, idx) => (
            filters.meal[key] ?  
            <span key={idx} className="tag is-dark">
                {key}
                <button onClick={() => dispatch(filter_update("meal", key, false))} className="delete is_small"></button>
            </span>
            : ""
          ))}
          {Object.keys(filters.diet).map((key, idx) => (
            filters.diet[key] ?  
            <span key={idx} className="tag is-dark">
                {key}
                <button onClick={() => dispatch(filter_update("diet", key, false))} className="delete is_small"></button>
            </span>
            : ""
          ))}
      </div>
      */}
    </div>
  );
}
