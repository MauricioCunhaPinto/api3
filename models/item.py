class ItemModel:
    def __init__(self, conn):
        self.conn = conn

    def create_item(self, item):
        cursor = self.conn.cursor()
        query = "INSERT INTO items (name, description) VALUES (%s, %s)"
        cursor.execute(query, (item.name, item.description))
        self.conn.commit()
        item.id = cursor.lastrowid
        cursor.close()
        return item

    def read_item(self, item_id):
        cursor = self.conn.cursor()
        query = "SELECT id, name, description FROM items WHERE id=%s"
        cursor.execute(query, (item_id,))
        item = cursor.fetchone()
        cursor.close()
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"id": item[0], "name": item[1], "description": item[2]}

    def update_item(self, item_id, item):
        cursor = self.conn.cursor()
        query = "UPDATE items SET name=%s, description=%s WHERE id=%s"
        cursor.execute(query, (item.name, item.description, item_id))
        self.conn.commit()
        cursor.close()
        item.id = item_id
        return item

    def delete_item(self, item_id):
        cursor = self.conn.cursor()
        query = "DELETE FROM items WHERE id=%s"
        cursor.execute(query, (item_id,))
        self.conn.commit()
        cursor.close()
        return {"id": item_id}