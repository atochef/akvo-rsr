/** @jsx React.DOM */

// Akvo RSR is covered by the GNU Affero General Public License.
// See more details in the license.txt file located at the root folder of the
// Akvo RSR module. For additional details on the GNU license please see
// < http://www.gnu.org/licenses/agpl.html >.

var filtersWrapper = document.getElementById('wrapper');

var TypeaheadClass = ReactBootstrapTypeahead.Typeahead;

var FilterClass = React.createClass({displayName: "FilterClass",
    render: function(){
        var Typeahead = React.createFactory(TypeaheadClass);
        return (
            React.createElement("div", null, 
                React.createElement("label", null, this.props.title), 
                React.createElement(Typeahead, {
                    selected: this.props.selected, 
                    options: this.props.data, 
                    onChange: this.onChange, 
                    filterBy: ['filterBy'], 
                    label: "label"}
                )
            )
        );
    },
    onChange: function(values){
        console.log("Filter values changed");
        console.log(values);
        this.props.onChange(values);
    }
});
var Filter = React.createFactory(FilterClass);

var FilterFormClass = React.createClass({displayName: "FilterFormClass",
    getInitialState: function(){
        return {
            "keyword": [],
            "location": [],
            "status": [],
            "organisation": [],
            "sector": [],
        };
    },
    componentDidMount: function(){
        this.fetchFilterData();
    },
    fetchFilterData: function(){
        var options = {};
        var self = this;
        fetch(this.props.data_url, options)
            .then(
                function(response){
                    if (response.status >=200 && response.status < 300) {
                        return response.json();
                    }
                }
            )
            .then(function(data){
                if (!data) {return;}
                self.setState(self.processData(data));
            });
    },
    processData: function(data){
        // Add a filterBy attribute to all items
        var make_typeahead_item = function(item){
            // Check various fields depending on type of data
            // NOTE: name always appears after long_name, since we
            // prefer long_name for organisations
            var label = item.label || item.long_name || item.name || '';
            item.filterBy = (label + ' ' + item.id).trim();
            item.label = label;
        };
        for (var key in data) {
            if (data.hasOwnProperty(key)) {
                var value = data[key];
                value.forEach(make_typeahead_item);
            }
        }
        return data;
    },
    onChange: function(values){
        console.log("values changed");
        console.log(values);
    },
    render: function(){
        var self = this;
        return (
            React.createElement("aside", {id: "sidebar-wrapper"}, 
                React.createElement("div", {id: "filter"}, 
                    this.props.filters.map(function(filter_name){
                         return (
                             React.createElement(Filter, {
                                 key: filter_name, 
                                 data: self.state[filter_name], 
                                 title: filter_name, 
                                 selected: [], 
                                 onChange: self.onChange}
                             )
                         );
                     }), 
                    React.createElement("div", null, 
                        React.createElement("nav", null, 
                            React.createElement("ul", {className: "nav nav-pills nav-stacked"}, 
                                /* FIXME: Use translation strings for 'apply filter' and 'close this' */
                                React.createElement("li", null, 
                                    /* FIXME: Button doesn't work */
                                    React.createElement("a", {className: "showFilters text-center", id: "apply-filter"}, "Apply filter")
                                ), 
                                React.createElement("li", null, 
                                    /* FIXME: Button doesn't work */
                                    React.createElement("a", {className: "showFilters menu-toggle text-center"}, 
                                        React.createElement("i", {className: "fa fa-toggle-off"}), "Close this"
                                    )
                                )
                            )
                        )
                    )
                )
            )
        );
    }
});


var FilterForm = React.createFactory(FilterFormClass);

var filters = ['keyword', 'location', 'status', 'organisation', 'sector'];
var url = 'http://rsr.localdev.akvo.org/rest/v1/typeaheads/project_filters?format=json';

document.addEventListener('DOMContentLoaded', function() {
    ReactDOM.render(
        React.createElement(FilterForm, {filters: filters, data_url: url}),
        filtersWrapper);
});
