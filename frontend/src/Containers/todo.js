import React from 'react';
import TodoPage from '../pages/todo';
import { TH_DISCONNECT } from '@blueprintjs/icons/lib/esm/generated/iconContents';

class Todo extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            items: [],
            newItemText: '',
        };

        this.onNewItem = this.onNewItem.bind(this);
        this.onRemoveItem = this.onRemoveItem.bind(this);
        this.onChangeNewItemText = this.onChangeNewItemText.bind(this);
        this.onExitEditMode = this.onExitEditMode.bind(this);
        this.onEnterEditMode = this.onEnterEditMode.bind(this);
        this.onToggleItemComplete = this.onToggleItemComplete.bind(this);
    }


    onNewItem() {
        this.setState({
            items: [
                ...this.state.items,
                {
                    id: Date.now(),
                    text: '',
                    isChecked: false,
                    isEditting: true, 
                },
            ],
        })
    }

    onRemoveItem(item) {
        const { items } = this.state;
        
        const index = items.findIndex(n => n.id === item.id);

        if (index === -1) {
            return;
        }
        const newItems = items.slice();
        newItems.splice(index, 1);

        this.setState({ items: newItems });
    }

    onChangeNewItemText(event) {
        this.setState({ newItemText: event.target.value });
    }

    onExitEditMode(item) {
        const {
            items,
            newItemText,
        } = this.state;

        this.setState({
            newItemText: '',
            items: items.map((next) => {
                if (next.id === item.id) {
                    return {
                        ...next,
                        isEditting: false,
                        text: newItemText,
                    };
                }

                return next;
            }),
        });
    }

    onEnterEditMode(item) {
        const {
            items,
            newItemText,
        } = this.state;

        this.setState({
            newItemText: item.text,
            items: items.map((next) => {
                if (next.id === item.id) {
                    return {
                        ...next,
                        isEditting: true,
                    };
                }

                return next;
            }),
        });
    }

    onToggleItemComplete(item) {
        const {
            items,
        } = this.state;

        this.setState({
            items: items.map((next) => {
                if (next.id === item.id) {
                    return {
                        ...next,
                        isChecked: !item.isChecked,
                    };
                }

                return next;
            }),
        });
    }

    render() {
        const {
            items,
            newItemText,
        } = this.state;

        return (
            <TodoPage
                items={items}
                newItemText={newItemText}
                onNewItem={this.onNewItem}
                onRemoveItem={this.onRemoveItem}
                onChangeNewItemText={this.onChangeNewItemText}
                onExitEditMode={this.onExitEditMode}
                onEnterEditMode={this.onEnterEditMode}
                onToggleItemComplete={this.onToggleItemComplete}
            />
        );
    }
}

export default Todo;